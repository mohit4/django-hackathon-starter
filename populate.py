#!/usr/bin/python

__author__      = "Mohit Kumar"
__version__     = "Beta"
__maintainer__  = "https://github.com/mohit4"
__email__       = "mohitkumar2801@gmail.com"

# assigning env variables from django project
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoHackathonStarter.settings')

# Setting up django configurations
import django
django.setup()

# python libraries for creating fake data
import random
from faker import Faker

# django app models for which data has to be populated
from django.contrib.auth.models import User
from app.models import Entity

# Initializing fake generator
fakegen = Faker()

def create_entities(N=10):
    '''
    Populate multiple entities here
    '''
    # get lists of all users in django db 
    # NOTE : Make sure at least one user exists, superuser will also work
    all_users = User.objects.all()

    # creating N entries
    for i in range(N):
        # generating fake data
        f_title = fakegen.sentence(nb_words=3)
        f_description = fakegen.sentence()
        f_points = random.randint(1,99)
        f_cost = round(random.uniform(10,99),2)
        f_category = random.choice([x[0] for x in Entity.CAT_CHOICES])
        f_active = random.choice([True, False])
        f_email = fakegen.email()
        f_user = random.choice(all_users)
        # creating data object and saving to DB
        entity = Entity(
            title=f_title,
            description=f_description,
            points=f_points,
            cost=f_cost,
            category=f_category,
            active=f_active,
            email=f_email,
            user=f_user
        )
        entity.save()
    
    # finished
    print("Finished...{} entries populated.".format(N))

if __name__ == "__main__":
    
    # Verify the number of command line arguments
    print("Initializing... checking syntax...")

    try:
        if len(sys.argv) == 2:
            N = int(sys.argv[1])
            print("Found parameter N = {}".format(N))
            # calling method for data population
            create_entities(N)
        else:
            print("No additional parameter provided, populating default no. of entries.")
            create_entities()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Exception occurred at line : {}! {}".format(exc_tb.tb_lineno, e))
        sys.exit(1)