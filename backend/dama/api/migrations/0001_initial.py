# Generated by Django 5.0.4 on 2024-10-28 00:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ONG',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=200)),
                ('contato_reponsavel', models.CharField(max_length=60)),
                ('tipo_servico', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=200)),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ONG',
                'verbose_name_plural': 'ONGs',
                'db_table': 'ong',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=128)),
                ('eh_ong', models.BooleanField(default=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('administrador', models.BooleanField(default=False)),
                ('ultimo_acesso', models.DateTimeField(blank=True, null=True)),
                ('ultima_atualizacao_senha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'usuario',
                'ordering': ['nome'],
            },
        ),
    ]
