# Generated by Django 3.0.4 on 2020-03-27 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_attractions', '0019_auto_20200327_0033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='touristattraction',
            old_name='id_document',
            new_name='identification_document',
        ),
        migrations.AlterField(
            model_name='touristattraction',
            name='guid',
            field=models.CharField(default='atboccgoyj', editable=False, max_length=10),
        ),
    ]
