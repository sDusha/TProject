# Generated by Django 4.0.4 on 2022-05-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_dictword_trashword_usersdictionary_dictword_word_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trashword',
            name='difficult',
            field=models.IntegerField(default=1, verbose_name='Сложность(1-10)'),
        ),
    ]
