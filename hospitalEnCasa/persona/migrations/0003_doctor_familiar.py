# Generated by Django 4.1.1 on 2022-09-11 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_paciente_fechanacimiento_persona_celular'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='persona.persona')),
                ('registro', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad', models.CharField(max_length=45)),
            ],
            bases=('persona.persona',),
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('paciente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.paciente')),
                ('parentesco', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
            ],
            bases=('persona.paciente',),
        ),
    ]
