# Generated by Django 5.0.6 on 2024-06-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
                ('Phone', models.CharField(max_length=11)),
                ('Address', models.TextField(max_length=90)),
                ('Location', models.TextField()),
            ],
        ),
    ]
