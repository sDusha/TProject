# Generated by Django 4.0.4 on 2022-05-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_trashword_english_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdictionary',
            name='words',
            field=models.ManyToManyField(blank=True, to='users.trashword'),
        ),
    ]