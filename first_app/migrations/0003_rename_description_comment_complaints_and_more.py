# Generated by Django 4.1 on 2022-09-18 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='complaints',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='reviews',
        ),
    ]