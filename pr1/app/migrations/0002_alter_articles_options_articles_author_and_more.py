# Generated by Django 4.1 on 2022-12-19 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец статьи'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(verbose_name='Дата смерти:'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(verbose_name='Вид смерти:'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Имя человека:'),
        ),
    ]