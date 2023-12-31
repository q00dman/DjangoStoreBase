# Generated by Django 4.2.4 on 2023-08-11 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0002_genre_technique"),
    ]

    operations = [
        migrations.AddField(
            model_name="goods",
            name="genre",
            field=models.ForeignKey(
                default="портрет",
                on_delete=django.db.models.deletion.CASCADE,
                to="apps.genre",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="goods",
            name="technique",
            field=models.ForeignKey(
                default="масляна",
                on_delete=django.db.models.deletion.CASCADE,
                to="apps.technique",
            ),
            preserve_default=False,
        ),
    ]
