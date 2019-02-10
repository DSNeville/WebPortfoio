# Generated by Django 2.0.2 on 2019-02-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('postimage', models.ImageField(default='', upload_to='images/')),
                ('blogpost', models.TextField()),
            ],
        ),
    ]
