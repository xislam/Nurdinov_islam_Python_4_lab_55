# Generated by Django 2.2.6 on 2019-10-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=31, verbose_name='teg'),
        ),
    ]
