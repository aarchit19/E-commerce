# Generated by Django 2.2.5 on 2020-01-29 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_remove_vendorprofileinfo_username_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custprofileinfo',
            name='username_cust',
        ),
    ]