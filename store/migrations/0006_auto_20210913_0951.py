# Generated by Django 3.2.7 on 2021-09-13 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='email_Adress',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='l_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
