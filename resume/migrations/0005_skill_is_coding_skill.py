# Generated by Django 4.2.3 on 2023-07-22 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_skill_is_key_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_coding_skill',
            field=models.BooleanField(default=False),
        ),
    ]
