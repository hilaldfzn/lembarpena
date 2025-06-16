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

# Copy static files to the correct directory for Vercel
echo "Copying static files for Vercel..."
mkdir -p staticfiles/static
mkdir -p staticfiles/media

# Ensure static files are in the right place
if [ -d "staticfiles" ]; then
    echo "Static files directory created successfully"
    ls -la staticfiles/
else
    echo "Error: Static files directory not found"
fi

echo "Build process completed!"