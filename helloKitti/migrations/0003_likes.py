# Generated by Django 4.2.2 on 2023-08-14 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("helloKitti", "0002_rename_likedat_commentlikes_liked_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Likes",
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
                (
                    "liked_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Liked at"),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="helloKitti.blogs",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="helloKitti.users",
                    ),
                ),
            ],
        ),
    ]
