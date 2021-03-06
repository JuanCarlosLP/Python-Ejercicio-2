# Generated by Django 2.2.19 on 2021-04-13 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permisos', '0001_initial'),
        ('puestos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('permiso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empleados', to='permisos.Permiso')),
                ('puesto', models.ManyToManyField(related_name='empleados', to='puestos.Puesto')),
            ],
        ),
    ]
