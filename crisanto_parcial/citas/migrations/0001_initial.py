# Generated by Django 4.2.1 on 2023-06-04 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_doctor', models.CharField(max_length=255, null=True)),
                ('doctor_direccion', models.CharField(max_length=255)),
                ('doctor_telefono', models.CharField(max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'doctores',
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad_nombre', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'especialidades',
            },
        ),
        migrations.CreateModel(
            name='TipoDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento_nombre', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Tipos_Documento_identidad',
            },
        ),
        migrations.CreateModel(
            name='TipoSeg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_seguro_nombre', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tipos_seguro',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('nro_documento', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255, null=True)),
                ('nacimiento', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tipo_documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.tipodoc')),
                ('tipo_seguro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.tiposeg')),
            ],
            options={
                'db_table': 'pacientes',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('observaciones', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.doctor')),
                ('especialidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.especialidad')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.paciente')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'citas_medicas',
            },
        ),
    ]
