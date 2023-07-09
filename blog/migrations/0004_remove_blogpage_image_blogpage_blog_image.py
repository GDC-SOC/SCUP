# Generated by Django 4.1.3 on 2023-04-10 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('blog', '0003_blogpage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='image',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='blog_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
