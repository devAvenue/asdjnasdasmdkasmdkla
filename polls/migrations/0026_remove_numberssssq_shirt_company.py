# Generated by Django 3.2.4 on 2021-06-14 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_alter_numberssssq_shirt_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numberssssq',
            name='shirt_company',
        ),
    ]
