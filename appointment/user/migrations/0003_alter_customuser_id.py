# Generated by Django 3.2.3 on 2021-08-11 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e28885c0-88d7-4883-8160-b2aeffd46f89'), editable=False, primary_key=True, serialize=False),
        ),
    ]
