from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import EnglishWord, KnownWords, CustomUser, UsersDictionary, TrashWord, DictWord, DictWordId
from .forms import EnglishForm, CustomUserCreationForm, UserLoginForm, CustomUserChangeForm, DictForm, TrashWordForm
from random import randint
import re


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {'title': 'Вход', 'form': form}
    return render(request, 'new_project/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная регистрация')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = CustomUserCreationForm()
    context = {'title': 'Регистрация', 'form': form}
    return render(request, 'new_project/registration.html', context)


def change_known(english_word: str, current_user: CustomUser, right_answer: bool):
    word_instance = EnglishWord.objects.filter(english_word=english_word)[0]
    if current_user.words.filter(word=word_instance).exists():
        known_word = current_user.words.get(word=word_instance)
    else:
        known_word = KnownWords.objects.create(word=word_instance, KnownPercent=0)
        known_word.save()
        current_user.words.add(known_word)
    known_word.KnownPercent += 10 if right_answer else -10
    if known_word.KnownPercent < 0:
        known_word.KnownPercent = 0
    elif known_word.KnownPercent > 100:
        known_word.KnownPercent = 100
    known_word.save()


def english(request):
    error = ''
    if request.user.is_authenticated:
        r = CustomUser.objects.get(id=request.user.id).word_id
        points = CustomUser.objects.get(id=request.user.id).words_points
        if r == -1:
            r = randint(0, len(EnglishWord.objects.all()) - 1)
            CustomUser.objects.filter(id=request.user.id).update(word_id=r)
    if request.method == 'POST':
        user_answer: str = request.POST['user_answer'].lower().strip().replace('ё', 'е')
        current_user: CustomUser = CustomUser.objects.get(id=request.user.id)
        print(request.POST['user_answer'], ' ', EnglishWord.objects.all()[r].russian_word)
        if user_answer in EnglishWord.objects.all()[r].russian_word.split():
            error = 'Верно'
            points += EnglishWord.objects.all()[r].difficult * 100
            change_known(EnglishWord.objects.all()[r].english_word, current_user, True)
            if points < 0:
                points = 0
            if CustomUser.objects.get(id=request.user.id).words_points_record < points:
                CustomUser.objects.filter(id=request.user.id).update(words_points_record=points)
            if request.user.is_authenticated:
                CustomUser.objects.filter(id=request.user.id).update(words_points=points)
        else:
            error = 'Неверно'
            points -= (10 - EnglishWord.objects.all()[r].difficult) * 100
            change_known(EnglishWord.objects.all()[r].english_word, current_user, False)
            if points < 0:
                points = 0
            if request.user.is_authenticated:
                CustomUser.objects.filter(id=request.user.id).update(words_points=points)
            else:
                points = 0
        r = randint(0, len(EnglishWord.objects.all()) - 1)
        CustomUser.objects.filter(id=request.user.id).update(word_id=r)
    else:
        points = CustomUser.objects.get(id=request.user.id).words_points
    words = EnglishWord.objects.all()[r]  # order_by по сложности можно
    top = CustomUser.objects.all().order_by('words_points_record')[::-1]
    context = {'title': 'Английский', 'error': error, 'words': words, 'points': points, 'top_users': top[3:10],
               'first': top[0], 'second': top[1], 'third': top[2]
               }
    return render(request, 'new_project/english.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = EnglishForm(request.POST)
        if form.is_valid() and re.match(r'[а-я]', form.cleaned_data['russian_word'])\
                and re.match(r'[a-z]', form.cleaned_data['english_word']):
            form.save()
            #  return redirect('english')
        else:
            error = 'форма была неверной'
    form = EnglishForm()
    words = EnglishWord.objects.all()[::-1][:10]
    context = {'title': 'Создать', 'form': form, 'error': error, 'words': words}
    return render(request, 'new_project/create.html', context)


def home(request):
    context = {'title': 'Главная'}
    return render(request, 'new_project/home.html', context)


def profile(request):
    if request.user.is_authenticated:
        user_instance = CustomUser.objects.get(id=request.user.id)
        point = user_instance.words_points
        record_points = user_instance.words_points_record
        known_words = user_instance.words.all().order_by('KnownPercent').reverse()[:10]
        context = {'title': 'Профиль', 'points': point, 'record_points': record_points, 'known_words': known_words}
        return render(request, 'new_project/profile.html', context)
    else:
        context = {'title': 'Домашняя страница'}
        return render(request, 'new_project/home.html', context)


def changeprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Успешное изменение')
                return redirect('profile')
            else:
                messages.error(request, 'Ошибка в изменение')
        else:
            data = CustomUser.objects.get(id=request.user.id)
            form = CustomUserChangeForm()
            form = CustomUserChangeForm(initial={'username': data.username, 'first_name': data.first_name,
                                                 'last_name': data.last_name, 'email': data.email})
        context = {'title': 'Регистрация', 'form': form}
        return render(request, 'new_project/changeprofile.html', context)
    else:
        context = {'title': 'Домашняя страница'}
        return render(request, 'new_project/home.html', context)


def add_word(request):
    error = ''
    dict_id = 1
    if request.method == 'POST':
        form = TrashWordForm(request.POST)
        if form.is_valid() and re.match(r'[а-я]', form.cleaned_data['russian_word'])\
                and re.match(r'[a-z]', form.cleaned_data['english_word']):
            english_word = form.cleaned_data['english_word']
            form.save()
            word = TrashWord.objects.all()[::-1][0]
            cur_dict = UsersDictionary.objects.get(name=request.POST['dict_name'])
            cur_dict.words.add(word)
            dict_id = cur_dict.id
            #  return redirect('english')
        else:
            error = 'форма была неверной'
    else:
        dict_id = request.GET['dict_id']
    form = TrashWordForm()
    words = UsersDictionary.objects.get(id=dict_id).words.all()[::-1][:10]
    # words = TrashWord.objects.all()[::-1][:10]
    if request.user.is_staff:
        dicts = UsersDictionary.objects.all()
    else:
        dicts = UsersDictionary.objects.filter(creator_id=request.user.id)
    context = {'title': 'Создать', 'form': form, 'error': error, 'words': words, 'dicts': dicts,
               'dict_id': int(dict_id)}
    return render(request, 'new_project/add_word.html', context)


def createdict(request):
    id_dict = 1
    name = ''
    #dict_words = UsersDictionary.objects.get(id=id_dict).words.all()
    #print(UsersDictionary.objects.get(id=id_dict))
    #for el in dict_words:
    #    print(el.word.russian_word + ' ' + el.word.english_word)
    error = ''
    if request.method == 'POST':
        form = DictForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_word')
        else:
            error = 'форма была неверной'
    form = DictForm()
    context = {'title': 'Создать', 'form': form, 'error': error}
    return render(request, 'new_project/createdict.html', context)


#изменение уровня знания слова из конкретного словаря
def change_known_dict(english_word: str, current_user: CustomUser, right_answer: bool):
    word_instance = EnglishWord.objects.filter(english_word=english_word)[0]
    if current_user.words.filter(word=word_instance).exists():
        known_word = current_user.words.get(word=word_instance)
    else:
        known_word = KnownWords.objects.create(word=word_instance, KnownPercent=0)
        known_word.save()
        current_user.words.add(known_word)
    known_word.KnownPercent += 10 if right_answer else -10
    if known_word.KnownPercent < 0:
        known_word.KnownPercent = 0
    elif known_word.KnownPercent > 100:
        known_word.KnownPercent = 100
    known_word.save()


#метод для проверки слов из словаря
def test(request):
    error = ''
    dict_id = 1
    if request =="POST":
        pass
    else:
        dict_id = request.GET['dict_id']
    context = {'title': 'Английский', 'error': error, 'dict_id': dict_id}
    return render(request, 'new_project/test.html', context)


def dicts(request):
    dicts = []
    all_dicts = UsersDictionary.objects.all()[::-1]
    if request.user.is_staff:
        dicts = UsersDictionary.objects.all()[::-1]
    else:
        dicts = UsersDictionary.objects.filter(creator_id=request.user.id)[::-1]
    error = ''
    context = {'title': 'Словари', 'error': error, 'dicts': dicts, "all_dicts": all_dicts}
    return render(request, 'new_project/dicts.html', context)


def watch_word(request):
    dict_id = 1
    if request.method == "GET":
        dict_id = request.GET['dict_id']
    words = UsersDictionary.objects.get(id=dict_id).words.all()
    dict_name = UsersDictionary.objects.get(id=dict_id).name
    error = ''
    context = {'title': 'Словари', 'error': error, 'words': words, 'dict_name': dict_name}
    return render(request, 'new_project/watch_word.html', context)