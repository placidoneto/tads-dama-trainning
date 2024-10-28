from factory.django import DjangoModelFactory
from factory import Faker
from api.models.usuario import Usuario

class UsuarioFactory(DjangoModelFactory):
    class Meta:
        model = Usuario

    nome = Faker('name')
    email = Faker('email')
    eh_ong = Faker('boolean')
    ativo = True
    administrador = Faker('boolean')
