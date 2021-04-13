# Generated by Django 3.1.1 on 2021-04-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210401_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='kod',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('1', 'Primary School'), ('2', 'High School'), ('3', 'University'), ('4', 'College')], max_length=200),
        ),
    ]
