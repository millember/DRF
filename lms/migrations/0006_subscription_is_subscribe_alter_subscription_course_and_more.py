# Generated by Django 5.1.2 on 2024-11-08 15:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0005_subscription"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="is_subscribe",
            field=models.BooleanField(default=False, verbose_name="подписка"),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscription_course",
                to="lms.course",
                verbose_name="Курс",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscription_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]