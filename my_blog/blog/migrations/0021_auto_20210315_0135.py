# Generated by Django 3.1.7 on 2021-03-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20210315_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='issue',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='volume',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
