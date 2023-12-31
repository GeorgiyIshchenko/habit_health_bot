# Generated by Django 4.2.3 on 2023-08-12 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_remove_notification_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bot.basepost')),
                ('aim', models.TextField(blank=True, null=True, verbose_name='Цель')),
                ('reward1', models.TextField(blank=True, null=True, verbose_name='Награда за 1-кратное выполнение')),
                ('reward30', models.TextField(blank=True, null=True, verbose_name='Награда за 30-кратное выполнение')),
            ],
            options={
                'verbose_name': 'Кастомная привычка',
                'verbose_name_plural': 'Кастомные привычки',
            },
            bases=('bot.basepost',),
        ),
    ]
