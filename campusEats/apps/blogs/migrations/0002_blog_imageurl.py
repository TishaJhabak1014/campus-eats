# Generated by Django 4.2.5 on 2023-10-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imageURL',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
