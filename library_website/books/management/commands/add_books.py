import csv

from books.models import Book
from django.core.management import BaseCommand


def get_data():
    books = []
    with open("books/fixtures/books.csv", newline="", encoding='utf-8-sig') as loc_file:
        reader = csv.DictReader(loc_file)
        for row in reader:
            books.append(row)
    return books


# The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Provide help at command prompt for user
    help = "Adds books"

    # A command must define handle()
    def handle(self, *args, **options):

        books = get_data()
        for book in books:
            Book.objects.get_or_create(
                title=book["title"],
                subtitle=book["subtitle"],
                author=book["author"],
                isbn=book["isbn"]
                )

        self.stdout.write(f"Total books added: {len(books)}")
