
# Tickets

Barber api

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

## Basic Commands

### Building then  images (only the first time or when you make changes to the Dockerfile)

      $ docker compose -f local.yml up --build

After thay you can run the following command to start the containers:

      $ docker compose -f local.yml up

### Create superuser

Run

    $ docker compose -f local.yml run --rm django python manage.py createsuperuser

Run Migration

    $ docker compose -f local.yml run --rm django python manage.py migrate



## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

Important add key for Cloudinary in .envs/.django 