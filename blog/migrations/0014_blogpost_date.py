# Generated by Django 3.1.5 on 2021-02-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210219_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
