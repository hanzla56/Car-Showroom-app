# Generated by Django 4.2.3 on 2023-07-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0008_alter_engine_number_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="contact_no",
            field=models.CharField(max_length=14),
        ),
    ]
