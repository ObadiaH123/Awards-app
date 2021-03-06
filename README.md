
## Author

KIPROTICH BETT

## Description
This is a django-python application where developers can upload their projects and peers can review and rate them. Projects are reviewed and rated according to usability, design and content.
## API Endpoints (url / uri)
    - CRUD : Create, Retrieve, Update, Delete 
    - Create List and Search

## HTTP methods (client side)
    - GET, POST, PUT, MATCH, DELETE    
    
## Data Types and Validation
    Use a serializer for consistency 
    JSON -> Serializer
    Validation -> Serializer
    
    
 
# Project prompt


A project can be rated based on 3 different criteria
  
    Design
    Usability
    Content
 
    These criteria can be reviewed on a scale of 1-10 and the average score is taken.

# User stories
As a user, you can:

    View posted projects and their details.
    Post a project to be rated/reviewed
    Rate/ review other users' projects
    Search for projects 
    View projects overall score
    View my profile page.

## System Features/Objectives

###  Projects

Projects  have a Title, an image of the project's landing page, a detailed description of the project, a link to the live site.

### Profile
Project have a user profile that has the following information:

    Profile picture of the user.
    User Bio
    Projects the user has posted
    A contact information of the user. 
    An Authentication System 

    The application  have a solid authentication system that allows users to sign up or log in to the application before posting or rating a project.



 
##  API Endpoints
    You should create an API so that users can access data from your application. You can create two API endpoints:

Profile - This endpoint return all the user profiles with information such as the username, bio, projects of the user and profile picture
Projects- This endpoint return information pertaining to all the projects posted in your application.


# Getting Started.

    These instructions will get you a copy of the project up and running on a local host
    Step 1: git clone
    Step 2: Enter the Project root folder

    cd gallery/
    install virtual environment (venv) without pip

    python3.6 -m venv --without-pip virtual
    Step 3: Activate virtual environment

    source virtual/bin/activate
    install pip using curl

## Deployment

    Deploying the Django Apps to Heroku to view.

## Built With

    Python3.8 - Python is a programming language that lets you work quickly and integrate systems more effectively
    Django - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design
    postgresql - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.


##  Known-Bugs

    Cannot search for projects

Copyright (c) 2021 Benard Kiprotich Bett

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


