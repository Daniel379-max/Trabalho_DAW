# Generated by Django 3.2.4 on 2021-06-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='porc2',
            field=models.IntegerField(blank=True, default=1, verbose_name='Porcentagem 2'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='porc3',
            field=models.IntegerField(blank=True, default=1, verbose_name='Porcentagem 3'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='porc4',
            field=models.IntegerField(blank=True, default=1, verbose_name='Porcentagem 4'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='porc5',
            field=models.IntegerField(blank=True, default=1, verbose_name='Porcentagem 1'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='porc6',
            field=models.IntegerField(blank=True, default=1, verbose_name='Porcentagem 2'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='porc7',
            field=models.IntegerField(blank=True, default=1, verbose_name='Porcentagem 3'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='porc8',
            field=models.IntegerField(blank=True, default=1, verbose_name='Porcentagem 4'),
        ),
    ]
