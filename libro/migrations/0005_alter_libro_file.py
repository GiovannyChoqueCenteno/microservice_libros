# Generated by Django 4.1.3 on 2022-11-29 23:05

from django.db import migrations, models
import libro.models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_remove_detalleprestamo_notaprestamo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='file',
            field=models.FileField(blank=True, upload_to=libro.models.upload_to_pdfs),
        ),
    ]
