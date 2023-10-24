"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """ ""Command to wait for the DB"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(
                    "Database unavailable, will retry after some seconds..."
                )
                time.sleep(5)

        self.stdout.write(self.style.SUCCESS("Database ready!"))
