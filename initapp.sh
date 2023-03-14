#!/bin/bash

# Create a new virtual environment (optional)
#python -m venv myenv

# Activate the virtual environment
#source myenv/bin/activate

# Install Django
pip install django

# Create a new Django project named SafeChatBackend
#django-admin startproject SafeChatBackend

# Navigate into the project directory
#cd SafeChatBackend

# Create a new Django app for the accounts feature
python manage.py startapp accounts

# Create a new Django app for the chats feature
python manage.py startapp chats

# Create a new directory for the static files
mkdir static

# Create a new directory for the templates
mkdir templates

# Create a new directory for the media files
mkdir media

# Create a new directory for the tests
mkdir tests

# Create a new directory for the deployment configuration files
mkdir deployment

# Initialize a new Git repository
git init

# Add all files to the Git repository
git add .

# Commit the initial changes
git commit -m "Initial commit"

# Create a new repository on GitHub

# Connect your local repository to the remote repository on GitHub
git remote add origin git@github.com:AKnuazev/SafeChatBackend

echo "Setup complete."
