# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings


class DatabaseRouter(object):
    app_name = "redmine_models"

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_name:
            return settings.REDMINE_DATABASE

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_name:
            return settings.REDMINE_DATABASE

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == settings.REDMINE_DATABASE:
            return app_label == self.app_name
        elif app_label == self.app_name:
            return False
