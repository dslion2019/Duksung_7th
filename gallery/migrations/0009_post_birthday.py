# Generated by Django 2.2.1 on 2019-05-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_remove_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='birthday',
            field=models.DateTimeField(auto_now=True),
        ),
    ]