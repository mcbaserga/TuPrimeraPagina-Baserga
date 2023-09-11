# Generated by Django 4.2.4 on 2023-09-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_rename_course_curso_delete_contactinfo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
            ],
        ),
    ]