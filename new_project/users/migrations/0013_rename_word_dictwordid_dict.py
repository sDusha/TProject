# Generated by Django 4.0.4 on 2022-05-27 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_dictwordid_customuser_id_dict_words'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictwordid',
            old_name='word',
            new_name='dict',
        ),
    ]
