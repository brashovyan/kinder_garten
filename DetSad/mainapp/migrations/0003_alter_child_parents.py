# Generated by Django 4.0.4 on 2022-05-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_child_secondname_alter_child_parents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parents',
            field=models.ManyToManyField(help_text='Выберите родителей ребенка', to='mainapp.parent', verbose_name='Родители'),
        ),
    ]
