# Generated by Django 2.2.16 on 2022-04-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composition', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='titles',
            options={'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.RemoveField(
            model_name='titles',
            name='year',
        ),
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.TextField(),
        ),
    ]