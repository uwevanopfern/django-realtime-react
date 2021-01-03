# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=no-member
from django.contrib import admin

from .models import Note

admin.site.register(Note)
