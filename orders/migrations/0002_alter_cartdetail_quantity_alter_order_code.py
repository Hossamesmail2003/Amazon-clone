# Generated by Django 5.1.2 on 2024-11-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='6YYSUXJM', max_length=10),
        ),
    ]
