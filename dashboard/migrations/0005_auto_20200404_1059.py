# Generated by Django 3.0.4 on 2020-04-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_measurement_bodytemperature'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthCustodianHashes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userHash', models.SlugField(default='test_hash', max_length=100)),
                ('reviewStatus', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Measurement',
            new_name='Measurements',
        ),
    ]