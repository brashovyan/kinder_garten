# Generated by Django 4.0.4 on 2022-05-18 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Garten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='Введите номер детского сада', verbose_name='Номер дет. сада')),
                ('title', models.CharField(help_text='Введите название дет. сада', max_length=150, verbose_name='Название')),
                ('director', models.CharField(help_text='Введите директора дет. сада', max_length=150, verbose_name='Директор')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название организации доп. образования', max_length=150, verbose_name='Организация')),
                ('director', models.CharField(help_text='Введите директора организации', max_length=150, null=True, verbose_name='Директор')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название секции', max_length=150, verbose_name='Секция')),
                ('date', models.DateField(help_text='Введите дату начала', verbose_name='Дата')),
                ('coach', models.CharField(help_text='Введите главного тренера секции', max_length=150, null=True, verbose_name='Тренер')),
                ('load', models.FloatField(default=10, help_text='Введите нагруженность секции', verbose_name='Нагруженность секции')),
                ('organization', models.ForeignKey(help_text='Выберите организацию', on_delete=django.db.models.deletion.CASCADE, to='mainapp.organization', verbose_name='Организация')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Родитель')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(help_text='Введите имя ребенка', max_length=50, verbose_name='Имя')),
                ('Lastname', models.CharField(help_text='Введите фамилию ребенка', max_length=50, verbose_name='Фамилия')),
                ('Secondname', models.CharField(help_text='Введите отчество ребенка', max_length=50, null=True, verbose_name='Отчество')),
                ('date', models.DateField(help_text='Введите дату рождения', verbose_name='Дата рождения')),
                ('number', models.IntegerField(help_text='Введите номер группы', verbose_name='Группа')),
                ('load', models.FloatField(default=0, help_text='Введите нагруженность ребенка', verbose_name='Нагруженность ребенка')),
                ('garten', models.ForeignKey(help_text='Выберите дет. сад', on_delete=django.db.models.deletion.CASCADE, to='mainapp.garten', verbose_name='Дет. сад')),
                ('parents', models.ManyToManyField(help_text='Выберите родителей ребенка', to='mainapp.parent', verbose_name='Родители')),
                ('sections', models.ManyToManyField(help_text='Выберите секции ребенка', to='mainapp.section', verbose_name='Секции')),
            ],
        ),
    ]
