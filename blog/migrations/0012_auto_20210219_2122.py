# Generated by Django 3.1.5 on 2021-02-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210219_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='topic',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]