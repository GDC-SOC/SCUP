# Generated by Django 4.1.3 on 2023-04-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpage_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='summary',
            field=models.CharField(max_length=500, null=True),
        ),
    ]