# Generated by Django 4.1.7 on 2023-04-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]