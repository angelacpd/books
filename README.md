# Books
Build a Bookstore with Django web framework, PostgreSQL database and Docker.

Based on book **Django for Professionals**:
https://wsvincent.com/books/

## Dependencies

Start `pipenv` environment
> pipenv shell

Install packages
> pipenv install

## Environment variables

Copy .env-example into the .env file
> cp .env-example .env

Change the environment variables in the .env file accordingly.

### SECRET_KEY
Generate settings.SECRET_KEY for your project and add it to the .env file.

Open shell
> python manage.py shell

Get the key by running the following function
```python
from django.core.management.utils import get_random_secret_key  

get_random_secret_key()
```

## Container

Build docker image
> docker build .

Start up container (detached)
> docker-compose up -d --build
