import random

from django.db import transaction
from django.core.management.base import BaseCommand

from accounts.models import *
from accounts.factories import *

NUM_USERS = 0
NUM_MUSICS = 120


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [User, Music]

        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        musics = []
        for _ in range(NUM_USERS):
            person = UserGenerator()
            people.append(person)

        # Add some users to clubs
        for _ in range(NUM_MUSICS):
            music = MusicGenerator()
            musics.append(music)
