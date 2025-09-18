from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Beachfront Villa",
                "description": "Enjoy the ocean view in this luxurious villa.",
                "price_per_night": 250.00,
                "location": "Malibu, USA",
            },
            {
                "title": "Mountain Cabin",
                "description": "Cozy cabin surrounded by pine trees.",
                "price_per_night": 120.00,
                "location": "Aspen, USA",
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "price_per_night": 90.00,
                "location": "New York, USA",
            },
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"{listing.title} already exists"))
