# Generated by Django 4.2.5 on 2023-10-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_reaction_review_user_reactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='extra',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_reactions',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
