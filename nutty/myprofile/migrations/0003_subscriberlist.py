# Generated by Django 3.2.4 on 2021-06-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriberlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
