# activate env
source env/bin/activate

### Please check the settings.py > DATABASES user and password and replace them for your credentials on your local machine

## Does the web application use Django to serve static HTML content?
* Yes the path to test it is: /restaurant/

## Has the learner committed the project to a Git repository?
* yes the commits are on github: https://github.com/danielsantiago1230/LittleLemon.git

## Does the application connect the backend to a MySQL database?
* the credentials are in settings.py > DATABASES, please replace your  'USER': 'root2', 'PASSWORD': '', to get this work on your local machine

## Are the menu and table booking APIs implemented?
* the path Menu /restaurant/menu/ and Booking /restaurant/booking/ or tables /restaurant/booking/tables/

## Is the application set up with user registration and authentication?
* yes I provide authentication for the Booking Apis not for Menu the path to get register a user is: /auth/users/
* getting a token by POST request with username & password on the payload:

## Does the application contain unit tests?
* python manage.py test command to run the tests
* the test folder in the project contains 2 test

## Can the API be tested with the Insomnia REST client?
* once your server is running you can test it with insonia Rest client