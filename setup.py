#!/usr/bin/python

__author__      = "Mohit Kumar"
__version__     = "Beta"
__maintainer__  = "https://github.com/mohit4"
__email__       = "mohitkumar2801@gmail.com"

# Python script to setup DHS for any project

import os
import sys
import fileinput

def setup_new_project(project_name):

    try:
        # Capitalizing
        project_name = project_name.capitalize()

        # file names and other constants
        text_to_search = 'DjangoHackathonStarter'
        manage_file = 'manage.py'
        populate_file = 'populate.py'
        wsgi_file = 'DjangoHackathonStarter/wsgi.py'
        settings_file = 'DjangoHackathonStarter/settings.py'

        # Renaming manage.py
        with fileinput.FileInput(manage_file, inplace=True) as file:
            for line in file:
                print(line.replace(text_to_search, project_name), end='')

        # Renaming populate.py
        with fileinput.FileInput(populate_file, inplace=True) as file:
            for line in file:
                print(line.replace(text_to_search, project_name), end='')

        # Renaming wsgi.py
        with fileinput.FileInput(wsgi_file, inplace=True) as file:
            for line in file:
                print(line.replace(text_to_search, project_name), end='')

        # Renaming settings.py
        with fileinput.FileInput(settings_file, inplace=True) as file:
            for line in file:
                print(line.replace(text_to_search, project_name), end='')

        # Renaming the folder
        os.rename(text_to_search,project_name)

    except Exception as e:
        print("Exception occured while performing rename : %s"%(e))
        sys.exit(0)

if __name__ == "__main__":

    # Name of new project
    project_name = ""

    # Look for the command line argument
    if len(sys.argv) > 1:
        project_name = str(sys.argv[1])
    else:
        print("No project name provided! Enter project name : ")
        project_name = str(input())
        print("Setting project name as : %s"%(project_name))
    
    setup_new_project(project_name)
    print("Finished!")