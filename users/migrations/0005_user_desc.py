# Generated by Django 4.0.10 on 2023-03-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_kakao_user_is_naver'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
