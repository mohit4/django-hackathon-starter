import time

from django.db import connections
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Command to check the availability of database
    """

    def handle(self, *args, **options):
        self.stdout.write( "Waiting for db..." )
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write( "Database unavailable, waiting for 1 sec..." )
                time.sleep(1)
        
        self.stdout.write( self.style.SUCCESS( "Database available!" ) )
