# Generated by Django 3.1.7 on 2021-03-24 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0005_topic_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='result',
        ),
    ]
