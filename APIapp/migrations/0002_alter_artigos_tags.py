# Generated by Django 5.1.5 on 2025-01-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigos',
            name='tags',
            field=models.JSONField(default=list),
        ),
    ]
