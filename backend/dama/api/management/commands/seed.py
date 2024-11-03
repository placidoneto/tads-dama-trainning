from api.models import Usuario, ONG 
from api.seed.ong import ONGFactory 
from api.seed.usuario import UsuarioFactory
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Crie usuários
        for _ in range(1000):  # Cria 10 usuários
            UsuarioFactory()

        # Crie ONGs
        for _ in range(10):  # Cria 5 ONGs
            ONGFactory()

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
