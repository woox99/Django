# Generated by Django 5.1.1 on 2024-09-27 23:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_book_publisher_book_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="publisher",
            field=models.CharField(max_length=100),
        ),
    ]
