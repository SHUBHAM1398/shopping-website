# Generated by Django 4.1.7 on 2023-04-09 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='name',
            new_name='email',
        ),
    ]
