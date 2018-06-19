# Django issue tracker

An issue tracker site with the following specification:

## Features

Issues can be added and the person who added the the issue is shown.

The issue has a text description, status and category, categories include:

    1. bug

    2. enhancements

    3. documentation



Issues can be added and edited via django admin.


Statistics about the average, longest and shortest time taken to solve the issues are shown in the header.


Categories are implemented in the database.


Django auth is used to implement a superuser who can change, add or edit any issues.

A staff account type (StaffUser in the model) can view issues but cannot edit or change anything.



## Database

SQLite


## Installation instructions

A virtualenv is required using python 3.6 along with all dependencies listed in requirements.txt


After activating your virtualenv dependencies can be installed with:

`pip install -r requirements.txt`


## Running the server and accessing the app

Navigate to issuesite and run:

`python manage.py runsever`
