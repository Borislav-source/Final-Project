# Generated by Django 3.2.6 on 2021-08-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='part', max_length=200),
            preserve_default=False,
        ),
    ]