# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, EnglishWord, KnownWords, DictWord, UsersDictionary, TrashWord


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'username', 'words_points']


class EnglishWordAdmin(admin.ModelAdmin):
    list_display = ('russian_word', 'english_word')


class KnownWordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'KnownPercent')


class TrashWordAdmin(admin.ModelAdmin):
    list_display = ('russian_word', 'english_word')


class UsersDictionaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator_id', 'difficult_lvl')


class DictWordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'KnownPercent')


admin.site.register(EnglishWord, EnglishWordAdmin)
admin.site.register(KnownWords, KnownWordsAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(DictWord, DictWordAdmin)
admin.site.register(UsersDictionary, UsersDictionaryAdmin)
admin.site.register(TrashWord, TrashWordAdmin)