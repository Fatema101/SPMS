# Generated by Django 4.1.7 on 2023-04-23 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_user',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=100)),
                ('User_type', models.CharField(max_length=30)),
            ],
        ),
    ]
