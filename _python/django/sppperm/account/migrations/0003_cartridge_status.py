# Generated by Django 3.0.6 on 2020-05-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_cartridge'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartridge',
            name='status',
            field=models.CharField(choices=[('draft', 'Проверяется'), ('published', 'Опубликован')], default='draft', max_length=10),
        ),
    ]