# Generated by Django 2.2.2 on 2019-06-16 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_comment_comment_approval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_approval',
        ),
    ]
