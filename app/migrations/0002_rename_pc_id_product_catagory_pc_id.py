# Generated by Django 4.2.2 on 2023-06-15 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product_catagory",
            old_name="Pc_id",
            new_name="pc_id",
        ),
    ]
