# Generated by Django 2.2.1 on 2019-06-01 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_auto_20190530_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='question.Board'),
        ),
    ]
