# Generated by Django 4.2.3 on 2023-07-18 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_book_total_rent_alter_book_photo_book_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='rental_price_day',
            new_name='rental_price_per_day',
        ),
    ]