# Generated by Django 4.1.3 on 2022-12-01 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_alter_question_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]