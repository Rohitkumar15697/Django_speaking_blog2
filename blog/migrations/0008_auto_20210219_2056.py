# Generated by Django 3.1.5 on 2021-02-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='topic',
            field=models.CharField(default=None, max_length=122),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
