# Generated by Django 5.1.4 on 2024-12-12 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.survey')),
            ],
        ),
    ]