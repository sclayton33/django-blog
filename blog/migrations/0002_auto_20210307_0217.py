# Generated by Django 3.1.7 on 2021-03-07 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='test-post', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]