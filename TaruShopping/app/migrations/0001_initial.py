# Generated by Django 5.0.6 on 2024-07-08 22:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=30)),
                ("selling_price", models.FloatField()),
                ("discount_price", models.FloatField()),
                ("description", models.TextField()),
                ("brand", models.CharField(max_length=40)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("M", "Mobile"),
                            ("L", "Lapetop"),
                            ("TW", "Top Wear"),
                            ("BW", "Bottom Wear"),
                        ],
                        max_length=10,
                    ),
                ),
                ("product_image", models.ImageField(upload_to="productimg")),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=100)),
                ("locality", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("zipcode", models.IntegerField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Mardan", " Mardan Mayar"),
                            ("Peshawer", "Peshawer"),
                            ("Islamabad", "Islamabad"),
                            ("Multan", "Multan"),
                            ("Karachi", "Karachi"),
                            ("Faisalabad", "Faisalabad"),
                            ("Mansehra", "Mansehra"),
                            ("Quetta", "Quetta"),
                            ("Gilgit", "Gilgit"),
                            ("Balochistan", "Balochistan"),
                            ("Rwalpindi", "Rwalpindi"),
                            ("Gujranalwala", "Gujranalwala"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderPlaced",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                ("order_date", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Packed", "Packed"),
                            ("On the way", "On the way"),
                            ("Cancel", "Cancel"),
                        ],
                        default="Pending",
                        max_length=30,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.customer"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
            ],
        ),
    ]