# Generated by Django 3.2.5 on 2021-07-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210721_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelo',
            old_name='nome',
            new_name='modelo',
        ),
        migrations.AlterField(
            model_name='modelo',
            name='marca',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
    ]
