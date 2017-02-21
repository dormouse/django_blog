

Install django::

    $ mkvirtualenv -p python3 django_blog
    $ pip install Django

Verify install in shell::

    $ python -m django --version
    1.10.5

Or in python shell::

    >>> import django
    >>> print(django.get_version())
    1.10.5

Creating a project::

    $ django-admin startproject django_site
    $ cd django_site

Run dev server at 127.0.0.1:8000::

    $ python manage.py runserver

Create app::

    $ python manage.py startapp blogs

Init models and database::

    $ python manage.py makemigrations polls
    $ python manage.py sqlmigrate polls 0001
    $ python manage.py migrate
    $ python manage.py createsuperuser

If you want to change the model you can:

- Change your models (in ``models.py``).
- Run ``python manage.py makemigrations`` to create migrations for those changes.
- Run ``python manage.py migrate`` to apply those changes to the database.


Play with shell
===============

Start django shell::

    $ python manage.py shell


