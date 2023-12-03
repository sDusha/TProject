# Generated by Django 4.0.4 on 2022-05-27 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_trashword_difficult'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictWordId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usersdictionary')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='id_dict_words',
            field=models.ManyToManyField(blank=True, to='users.dictwordid'),
        ),
    ]
