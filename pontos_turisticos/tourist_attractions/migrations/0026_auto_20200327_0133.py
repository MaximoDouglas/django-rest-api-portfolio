# Generated by Django 3.0.4 on 2020-03-27 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_attractions', '0025_auto_20200327_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristattraction',
            name='guid',
            field=models.CharField(default='qrosladzsu', editable=False, max_length=10),
        ),
    ]
