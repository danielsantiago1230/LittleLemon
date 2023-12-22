# LittleLemon - A Django-Driven Restaurant Application
## Overview
LittleLemon is a Django-based web application designed primarily to provide REST API services for restaurant operations. It facilitates the management of menus and table bookings, offering a streamlined solution for modern restaurant needs. This application demonstrates effective use of Django's capabilities in creating RESTful services, backed by a MySQL database for efficient data handling.

## Features
* Menu Management: Allows for easy listing, updating, and managing of restaurant menus.
* Table Booking System: Integrated booking system for hassle-free table reservations.
* User Authentication: Secure user registration and authentication for booking tables.
* API Endpoints: RESTful API endpoints for menu and booking operations, enabling seamless integration with other systems or third-party applications.

## Technology Stack
* Backend: Django, Django REST Framework
* Database: MySQL
* Authentication: Djoser for handling user authentication and token generation
* Testing: Comprehensive unit tests to ensure application reliability

## Getting Started
### Prerequisites
* Python
* MySQL Server

## Installation and Setup
1. Clone the Repository:
* git clone https://github.com/danielsantiago1230/LittleLemon.git
2. Create a Virtual Environment:
* python3 -m venv env_littlelemon or python -m venv env_littlelemon
* source env_littlelemon/bin/activate
3. Install Dependencies:
* pip install -r requirements.txt
4. Database Configuration: Update the settings.py file under the DATABASES section with your MySQL credentials.
5. Run Migrations:
* python manage.py migrate
6. Run server:
* python manage.py runserver

## Usage
* Menu Management: Accessible at .../restaurant/menu/.
* Table Booking: Book tables at .../restaurant/booking/ or .../restaurant/booking/tables/.
* User Registration and Authentication: Register at .../auth/users/ and obtain a token via a POST request with username & password to .../restaurant/api-token-auth/.

## Testing
* Run python manage.py test to execute unit tests.
* Test API endpoints using the Insomnia REST client after starting the server.