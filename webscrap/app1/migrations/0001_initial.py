# Generated by Django 4.2.10 on 2024-02-14 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criptodivisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('precio', models.DecimalField(decimal_places=20, max_digits=21)),
            ],
        ),
    ]
