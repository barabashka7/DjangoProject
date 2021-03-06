# Generated by Django 2.0.2 on 2018-02-10 11:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news_blog', '0002_auto_20180210_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cdc7c68e-28ab-4d5b-b01e-bb4845fdc69f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1867856a-1826-4b04-90af-f53c90736f74'), editable=False, primary_key=True, serialize=False),
        ),
    ]
