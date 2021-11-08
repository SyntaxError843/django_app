# Generated by Django 3.2.9 on 2021-11-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(default='', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('LBP', 'LBP')], default='USD', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
    ]