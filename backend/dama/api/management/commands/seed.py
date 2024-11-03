from django.core.management.base import BaseCommand
from api.models import Usuario, ONG, Relato
from api.seed.ong import ONGFactory 
from api.seed.usuario import UsuarioFactory
from api.seed.relato import RelatoFactory


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Crie usuários
        for _ in range(1000):  # Cria 10 usuários
            UsuarioFactory()

        # Crie ONGs
        for _ in range(10):  # Cria 5 ONGs
            ONGFactory()

        for _ in range(1000):
            RelatoFactory()

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
