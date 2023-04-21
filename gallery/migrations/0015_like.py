# Generated by Django 2.2.6 on 2019-10-08 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_auto_20190618_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.ManyToManyField(related_name='likes', to='gallery.Post')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_action', to='gallery.Post')),
            ],
        ),
    ]