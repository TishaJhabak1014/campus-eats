# Generated by Django 4.2.5 on 2023-10-26 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('user_type', models.CharField(choices=[('user', 'USER'), ('admin', 'ADMIN'), ('blogger', 'BLOGGER')], default='user', max_length=10)),
                ('contact_number', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('BookmarkID', models.AutoField(primary_key=True, serialize=False)),
                ('RestaurantID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
    ]
