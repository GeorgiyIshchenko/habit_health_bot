# Generated by Django 4.2.3 on 2023-08-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_alter_post_media_id_alter_reward_photo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='benefits',
            field=models.TextField(blank=True, null=True, verbose_name='🌱 Польза 🌳'),
        ),
        migrations.AlterField(
            model_name='post',
            name='relevance',
            field=models.TextField(blank=True, null=True, verbose_name='🔥 Актуальность 📣'),
        ),
        migrations.AlterField(
            model_name='post',
            name='req_time',
            field=models.TextField(blank=True, null=True, verbose_name='🕰 Рекомендованное время 🗓'),
        ),
        migrations.AlterField(
            model_name='post',
            name='reqs',
            field=models.TextField(blank=True, null=True, verbose_name='👍 Рекомендации 💡'),
        ),
        migrations.AlterField(
            model_name='post',
            name='technique',
            field=models.TextField(blank=True, null=True, verbose_name='📝 Техника выполнения ⚙️'),
        ),
    ]
