from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class EnglishWord(models.Model):
    russian_word = models.CharField("Слово на русском", max_length=100)
    english_word = models.CharField("Слово на английском", max_length=100, unique=True)
    difficult = models.IntegerField("Сложность(1-10)",  default=1)


class KnownWords(models.Model):
    word = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
    KnownPercent = models.IntegerField("Процент знания", default=0)


class TrashWord(models.Model):
    russian_word = models.CharField("Слово на русском", max_length=100)
    english_word = models.CharField("Слово на английском", max_length=100)
    difficult = models.IntegerField("Сложность(1-10)", default=1)


class DictWord(models.Model):
    word = models.ForeignKey(TrashWord, on_delete=models.CASCADE)
    KnownPercent = models.IntegerField("Процент знания", default=0)


class UsersDictionary(models.Model):
    name = models.CharField("Назване словаря", max_length=100, unique=True)
    password = models.CharField("Пароль для доступа", max_length=100, blank=True)
    creator_id = models.IntegerField("автор", default=1)
    creation_time = models.DateTimeField(auto_now_add=True)
    difficult_lvl = models.IntegerField("Сложность", validators=[MaxValueValidator(100), MinValueValidator(0)])
    words = models.ManyToManyField(TrashWord, blank=True)


class DictWordId(models.Model):
    dict = models.ForeignKey(UsersDictionary, on_delete=models.CASCADE)
    word = models.ForeignKey(DictWord, on_delete=models.CASCADE)


class CustomUser(AbstractUser):
    words = models.ManyToManyField(KnownWords, blank=True)
    word_id = models.IntegerField('id текущего слова', default=-1)
    words_points = models.IntegerField('Очков в словах', default=0)
    words_points_record = models.IntegerField('Рекорд в очках', default=0)
    photo = models.ImageField(upload_to='photos', default='photos/base.jpg')

    # Знание слов из пользовательских словарей
    dict_words = models.ManyToManyField(DictWord, blank=True)
    id_dict_words = models.ManyToManyField(DictWordId, blank=True)
