# Generated by Django 3.0.5 on 2020-04-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0002_records'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='verification',
            field=models.BooleanField(default=False),
        ),
    ]
