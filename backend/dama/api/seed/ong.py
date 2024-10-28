import factory
from factory import SubFactory, Faker
from factory.django import DjangoModelFactory
from api.models.ong import ONG
from .usuario import UsuarioFactory

class ONGFactory(DjangoModelFactory):
    class Meta:
        model = ONG
        django_get_or_create = ('nome',)
        exclude = ('data_criacao',)

    nome = Faker('company')
    responsavel = Faker('name')
    contato_reponsavel = Faker('email')
    tipo_servico = Faker('catch_phrase')
    localizacao = Faker('address')
    ativo = True
    usuario = SubFactory(UsuarioFactory)
