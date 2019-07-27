#!/usr/bin/python

__author__      = "Mohit Kumar"
__version__     = "Beta"
__maintainer__  = "https://github.com/mohit4"
__email__       = "mohitkumar2801@gmail.com"

# assigning env variables from django project
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoHackathonStarter.settings')

# Setting up django configurations
import django
django.setup()