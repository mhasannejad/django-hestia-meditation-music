# Generated by Django 3.1.7 on 2021-11-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
