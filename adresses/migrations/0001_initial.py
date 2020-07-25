# Generated by Django 3.0.4 on 2020-03-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('district', models.CharField(blank=True, max_length=150, null=True)),
                ('complement', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=70)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]