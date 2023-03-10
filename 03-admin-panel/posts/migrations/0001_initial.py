# Generated by Django 4.1.4 on 2022-12-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('Created_At', models.DateField(auto_now_add=True)),
                ('Update_At', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
