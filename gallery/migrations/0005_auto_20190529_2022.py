# Generated by Django 2.2.1 on 2019-05-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20190529_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='now_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]
