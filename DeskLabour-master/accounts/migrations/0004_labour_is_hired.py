# Generated by Django 3.2 on 2021-05-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_hiringlabour'),
    ]

    operations = [
        migrations.AddField(
            model_name='labour',
            name='is_hired',
            field=models.BooleanField(default=False),
        ),
    ]
