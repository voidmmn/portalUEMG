# Generated by Django 5.0.3 on 2024-03-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0002_alter_curso_coordenador'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='cursos/'),
        ),
    ]
