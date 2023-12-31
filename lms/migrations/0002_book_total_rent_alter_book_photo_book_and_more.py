# Generated by Django 4.2.3 on 2023-07-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo_book',
            field=models.ImageField(blank=True, default=' media/photos/photo1.png', null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('rented', 'rented'), ('sold', 'sold')], max_length=50, null=True),
        ),
    ]
