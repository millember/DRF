# Generated by Django 5.1.2 on 2024-11-10 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_rename_cost_payment_amount"),
    ]

    operations = [
        migrations.RenameField(
            model_name="payment",
            old_name="amount",
            new_name="payment_sum",
        ),
    ]