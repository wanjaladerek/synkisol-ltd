# Generated by Django 4.1.2 on 2022-10-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project_similar_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='similar_image',
            field=models.ImageField(default=2, upload_to='images/'),
            preserve_default=False,
        ),
    ]