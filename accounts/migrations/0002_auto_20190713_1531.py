# Generated by Django 2.1.7 on 2019-07-13 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='date_od_birth',
            new_name='date_of_birth',
        ),
    ]
