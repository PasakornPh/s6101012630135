# Generated by Django 3.0 on 2020-02-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='saveResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val_results', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='inputNumber',
        ),
    ]
