# Generated by Django 2.2.5 on 2020-07-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Career_choose',
            new_name='What_best_describe_you',
        ),
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.CharField(max_length=2048),
        ),
    ]
