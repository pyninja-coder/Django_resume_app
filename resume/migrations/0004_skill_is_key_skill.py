# Generated by Django 4.2.3 on 2023-07-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_media_alter_blog_options_alter_testimonial_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_key_skill',
            field=models.BooleanField(default=False),
        ),
    ]
