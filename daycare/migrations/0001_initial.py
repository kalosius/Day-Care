# Generated by Django 5.0.4 on 2024-04-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('work_type', models.CharField(choices=[('full_time', 'Full Time'), ('half_time', 'Half Time')], max_length=20)),
            ],
        ),
    ]
