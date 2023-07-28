# Generated by Django 4.2.3 on 2023-07-26 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0003_engine_number_car_engine_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="model",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="model",
                to="showroom.brand",
            ),
        ),
    ]
