# Generated by Django 2.1.4 on 2019-07-18 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModuloCompras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=10, max_digits=19)),
                ('provehedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ModuloCompras.Provehedor')),
            ],
        ),
    ]
