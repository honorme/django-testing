# django-testing

# Example Markdown content

markdown_content = """

# My API Documentation

## Introduction

This is the documentation for my Django Testing API.

## Endpoints

<!-- GET -->

- `https://django-testing-production.up.railway.app/api/${id}`: This is used to get a single person from the database.
- `https://django-testing-production.up.railway.app/api/`: This gets all persons from a database.
<!-- GET -->

<!-- POST -->

- `https://django-testing-production.up.railway.app/api/`: This is used to add a person.

e.g

<!-- the id is generated automatically -->

{
"name": "jack"
}

<!-- POST -->

<!-- PUT -->

e.g

<!-- the id is passed in the url -->

{
"name": "joe"
}

- `https://django-testing-production.up.railway.app/api/${id}`: This is used to update the details of a person.
<!-- PUT -->

<!-- DELETE -->

- `https://django-testing-production.up.railway.app/api/${id}`: This is used to delete a person from the database
<!-- DELETE -->

## Authentication

The api doesn't need authentication.

## Usage

Here's how you can use the API:

<!-- On localhost -->

To start the server, run `python manage.py runserver` in the terminal
By default the server runs on `http://127.0.0.1:8000/`
Then append `/api` to test the api

<!-- On localhost -->

To test the server live, use `https://django-testing-production.up.railway.app`

The postman script is located in the root of the Django testing folder `DjangoTesting.postman_collection.json` at this repo:
`https://github.com/honorme/django-testing/DjangoTesting.postman_collection.json`

## UML Diagram

The UML Diagram is in the root directory of the Django Testing folder in this repo: `https://github.com/honorme/django-testing/UML-Diagram.png`
