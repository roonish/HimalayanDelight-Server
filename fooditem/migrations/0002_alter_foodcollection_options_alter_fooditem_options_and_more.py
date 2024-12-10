# Generated by Django 5.1.4 on 2024-12-09 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodcollection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='fooditem',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='fooditem',
            name='rating',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]