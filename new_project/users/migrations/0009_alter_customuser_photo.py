# Generated by Django 4.0.4 on 2022-05-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(default='photos/base.jpg', upload_to='photos'),
        ),
    ]
