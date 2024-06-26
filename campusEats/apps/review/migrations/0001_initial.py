# Generated by Django 4.2.5 on 2023-10-26 06:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitReacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('ReviewID', models.AutoField(primary_key=True, serialize=False)),
                ('Rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('ParentReviewID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='review.review')),
                ('RestaurantID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
                ('UserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_reacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.initreacts')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
            options={
                'unique_together': {('id', 'user', 'review')},
            },
        ),
    ]
