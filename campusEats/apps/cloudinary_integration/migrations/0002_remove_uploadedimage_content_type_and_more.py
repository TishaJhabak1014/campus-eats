# Generated by Django 4.2.5 on 2023-10-27 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudinary_integration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='uploadedimage',
            name='object_id',
        ),
    ]
