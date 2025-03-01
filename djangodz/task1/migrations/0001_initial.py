# Generated by Django 5.1.4 on 2024-12-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.DecimalField(decimal_places=2, max_digits=15, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Имя пользователя')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Баланс')),
                ('age', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Bозраст пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.DecimalField(decimal_places=2, max_digits=15, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Наменование')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена')),
                ('size', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Размер файла')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('age_limited_gte', models.BooleanField(default=18)),
                ('buyer', models.ManyToManyField(blank=True, null=True, to='task1.buyer')),
            ],
        ),
    ]
