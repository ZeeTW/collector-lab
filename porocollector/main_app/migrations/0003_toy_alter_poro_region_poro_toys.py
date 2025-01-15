# Generated by Django 5.1.4 on 2025-01-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_poro_region_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='poro',
            name='region',
            field=models.CharField(choices=[('F', 'Freljord'), ('D', 'Demacia'), ('I', 'Ionia'), ('N', 'Noxus'), ('P', 'Piltover & Zaun'), ('S', 'Shadow Isles'), ('B', 'Bilgewater'), ('T', 'Targon'), ('SH', 'Shurima'), ('BC', 'Bandle City'), ('R', 'Runterra')], default='F', max_length=100),
        ),
        migrations.AddField(
            model_name='poro',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]