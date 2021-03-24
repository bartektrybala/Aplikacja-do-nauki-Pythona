# Generated by Django 3.1.7 on 2021-03-23 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(choices=[('1', 'Primary School'), ('2', 'High School'), ('3', 'University'), ('4', 'College'), ('5', 'WSRH')], max_length=200)),
                ('age', models.IntegerField()),
                ('profile_image', models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to='users/')),
                ('points', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
