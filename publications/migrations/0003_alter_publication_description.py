# Generated by Django 4.2.7 on 2023-11-09 22:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
