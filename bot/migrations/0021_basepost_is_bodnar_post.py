# Generated by Django 4.2.3 on 2023-08-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0020_alter_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='basepost',
            name='is_bodnar_post',
            field=models.BooleanField(default=True, verbose_name='Привычка Виталия (флаг)'),
        ),
    ]
