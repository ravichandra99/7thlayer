# Generated by Django 3.2.5 on 2021-07-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umasagar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salebilldetails',
            name='tcs',
            field=models.BooleanField(default=False),
        ),
    ]
