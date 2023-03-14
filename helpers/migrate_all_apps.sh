#!/bin/bash

# Activate virtual environment
source ../venv/bin/activate

# Change to project directory
cd /Users/antonknuazev/PycharmProjects/SafeChatBackend

# Make migrations for all apps
python manage.py makemigrations accounts chats

# Apply migrations
python manage.py migrate