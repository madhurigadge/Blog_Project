# Generated by Django 4.2.7 on 2023-12-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='mini_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
