# Generated by Django 4.2.3 on 2023-07-26 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0004_model_brand"),
    ]

    operations = [
        migrations.CreateModel(
            name="customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("pic", models.ImageField(blank=True, upload_to="")),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("address", models.CharField(blank=True, max_length=50, null=True)),
                ("contact_no", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stock",
                        to="showroom.brand",
                    ),
                ),
                (
                    "model",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stock",
                        to="showroom.model",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "brand_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale",
                        to="showroom.brand",
                    ),
                ),
                (
                    "chessis_no",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale",
                        to="showroom.car",
                    ),
                ),
                (
                    "customer_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sale",
                        to="showroom.customer",
                    ),
                ),
            ],
        ),
    ]
