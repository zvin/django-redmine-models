# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings


class DatabaseRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == "redmine_models":
            return settings.REDMINE_DATABASE

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "redmine_models":
            return settings.REDMINE_DATABASE

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == settings.REDMINE_DATABASE and app_label != "redmine_models":
            return False
