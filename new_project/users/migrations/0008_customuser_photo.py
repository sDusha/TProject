# Generated by Django 4.0.4 on 2022-05-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_word_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(default='photo/base.jpg', upload_to='photo/%Y/%m/%d'),
        ),
    ]