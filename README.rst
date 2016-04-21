=====================
django-redmine-models
=====================

.. image:: https://img.shields.io/pypi/v/django-redmine-models.svg
   :target: https://pypi.python.org/pypi/django-redmine-models
   :alt: PyPI Version


Using django-redmine-models
===========================

Define the database parameters as usual in the ``DATABASES`` setting then add::

    REDMINE_DATABASE = "the-redmine-db-key-in-DATABASES"

and define (or add) the database router::

    DATABASE_ROUTERS = ["redmine_models.routers.DatabaseRouter"]

Then use the models::

    from redmine_models.models import Project
    print Project.objects.all()
    # etc...
