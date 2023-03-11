# Generated by Django 4.1.7 on 2023-03-11 15:17

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
            name="Dong_list",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Gu_list",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Keyword",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "description",
                    models.TextField(blank=True, max_length=150, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="House",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100)),
                ("price", models.PositiveIntegerField(default=0)),
                ("room", models.PositiveIntegerField(default=0)),
                ("toilet", models.PositiveIntegerField(default=0)),
                ("pyeongsu", models.PositiveIntegerField(default=0)),
                ("distance_to_station", models.PositiveIntegerField(default=0)),
                (
                    "room_kind",
                    models.CharField(
                        choices=[
                            ("ONE_ROOM", "원룸"),
                            ("TWO_ROOM", "투룸"),
                            ("THREE_ROOM", "쓰리룸 이상"),
                            ("OFFICETEL", "오피스텔"),
                            ("APART", "아파트"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "cell_kind",
                    models.CharField(
                        choices=[
                            ("MONTHLY_RENT", "월세"),
                            ("CHARTER", "전세"),
                            ("SALE", "매매"),
                        ],
                        max_length=20,
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                ("photo", models.URLField(blank=True, null=True)),
                ("description", models.TextField(blank=True)),
                ("visited", models.PositiveIntegerField(default=0, editable=False)),
                ("is_sale", models.BooleanField(default=True)),
                (
                    "dong",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="houses.dong_list",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "realtor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="realtor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="dong_list",
            name="gu",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dong",
                to="houses.gu_list",
            ),
        ),
    ]
