# Generated by Django 5.1.4 on 2024-12-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("text", models.TextField()),
                ("sentiment", models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name="reviews",
        ),
    ]
