# Generated by Django 5.0.3 on 2024-03-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0004_alter_perfilusuario_cpf_and_more'),
        ('administrativo', '0003_curso_descricao_curso_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilusuario',
            name='papel',
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='papeis',
            field=models.ManyToManyField(blank=True, to='administrativo.papel'),
        ),
    ]
