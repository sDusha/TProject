from django.forms import ModelForm, TextInput, CharField, EmailField, EmailInput, PasswordInput, ImageField, FileInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, EnglishWord, UsersDictionary, TrashWord


class UserLoginForm(AuthenticationForm):
    username = CharField(label='Ник', widget=TextInput(attrs={'class': 'form-control', 'autocomplete': 'off',
                                                              'autofocus': None}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))


class CustomUserCreationForm(UserCreationForm):
    username = CharField(label='Ник', widget=TextInput(attrs={'class': 'form-control', 'autocomplete': 'off',
                                                              'autofocus': None}))
    first_name = CharField(label='Имя', widget=TextInput(attrs={'class': 'form-control'}))
    last_name = CharField(label='Фамилия', widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(label='E-mail', widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(label='Пароль еще раз', widget=PasswordInput(attrs={'class': 'form-control'}))
    # 'upload_to': 'media/photo'

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'photo')


class CustomUserChangeForm(ModelForm):
    username = CharField(label='Ник', widget=TextInput(attrs={'class': 'form-control', 'autocomplete': 'off',
                                                              'autofocus': None}))
    first_name = CharField(label='Имя', required=False, widget=TextInput(attrs={'class': 'form-control'}))
    last_name = CharField(label='Фамилия', required=False, widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(label='E-mail', required=False, widget=EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'photo', 'first_name', 'last_name')


class EnglishForm(ModelForm):
    class Meta:
        model = EnglishWord
        fields = ["russian_word", "english_word", "difficult"]
        widgets = {
            "russian_word": TextInput(attrs={
                'class': 'form-control',
                'style': 'text-transform:lowercase;',
                'placeholder': 'Введите слово на русском, если несколько переводов, то вводите через пробел'
            }),
            "english_word": TextInput(attrs={
                'class': 'form-control',
                'style': 'text-transform:lowercase;',
                'placeholder': 'Введите слово на английском'
            }),
            "difficult": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите сложность слова'
            })
            }


class DictForm(ModelForm):
    class Meta:
        model = UsersDictionary
        fields = ["name", "password", "creator_id", "difficult_lvl"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'style': 'text-transform:lowercase;',
                'placeholder': 'Название'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'style': 'text-transform:lowercase;',
                'placeholder': 'пароль'
            }),
            "creator_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор набора'
            }),
            "difficult_lvl": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите сложность словаря'
            })
            }


class TrashWordForm(ModelForm):
    class Meta:
        model = TrashWord
        fields = ["russian_word", "english_word", "difficult"]
        widgets = {
            "russian_word": TextInput(attrs={
                'class': 'form-control',
                'style': 'text-transform:lowercase;',
                'placeholder': 'Введите слово на русском, если несколько переводов, то вводите через пробел'
            }),
            "english_word": TextInput(attrs={
                'class': 'form-control',
                'style': 'text-transform:lowercase;',
                'placeholder': 'Введите слово на английском'
            }),
            "difficult": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите сложность слова'
            })
            }