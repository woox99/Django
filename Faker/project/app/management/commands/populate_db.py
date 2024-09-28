from django.core.management.base import BaseCommand
from app.models import Person

from faker import Faker

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):  # Adjust the range for the number of records you need
            Person.objects.create(
                name=fake.name(),
                address=fake.address(),
                email=fake.email(),
                # Add or change fields as needed
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data.'))
