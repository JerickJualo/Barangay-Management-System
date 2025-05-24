# Barangay Management System

# DEPLOYED URL BELOW!

A Django-based web application designed to manage the hierarchical data of a Barangay Amoslog in Placer, Surigao Del Norte:

Puroks, Streets, Households, and Residents. 
It supports full CRUD operations for residents, secure authentication, and a RESTful API for integration with other services.

# Prerequisites

* Python 3.8+
* pip (Python package installer)
* Git 
* Django Project
* (Optional) VS Code or your preferred IDE

# Features

- Hierarchical Models: Purok → Street → Household → Resident relationships
- CRUD Interfaces: Create, Read, Update, Delete residents via web UI and API
- Filtering & Search: Filter residents by Purok, Street, or Household directly in the list view
- Clean Theming: Orange & green responsive design with CSS variables for easy customization
- Authentication: Built-in login/logout; only admin can create new accounts
- REST API: DRF-powered endpoints with nested serializers and routers

# Installation

1. Clone the repo:
   
   git clone https://github.com/JerickJualo/barangay-management-system.git
   cd barangay-management-system

# Create & activate a virtual environment:

python3 -m venv env

source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies:

pip install -r requirements.txt

# Apply database migrations:

python manage.py migrate

# Create a superuser:

python manage.py createsuperuser

# Run the development server:

python manage.py runserver

# BARANGAY MANAGEMENT SYSTEM BY JUALO DEPLOYED URL:

# https://barangay-management-system-vsoj.onrender.com

# LOG-IN ACCOUNT:

# USERNAME: dummyacc
# PASSWORD: realpassword

