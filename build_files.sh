#!/bin/bash

# Update pip
echo "Updating pip..."
python3.9 -m pip install --upgrade pip

# Install dependencies
echo "Installing project dependencies..."
python3.9 -m pip install -r requirements.txt

# Make migrations
echo "Making migrations..."
python3.9 manage.py makemigrations --noinput

# Apply migrations
echo "Applying migrations..."
python3.9 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build process completed!"