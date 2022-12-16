# Generated by Django 4.0.4 on 2022-05-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MixDoc', '0009_os1'),
    ]

    operations = [
        migrations.CreateModel(
            name='os2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_img2', models.ImageField(default='', upload_to='static/images/')),
                ('os_title2', models.CharField(max_length=30)),
                ('os_discription2', models.CharField(max_length=100)),
                ('os_moreinfo2', models.CharField(max_length=200)),
                ('os_download2', models.CharField(max_length=500)),
            ],
        ),
    ]