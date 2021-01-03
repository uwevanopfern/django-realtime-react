# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=no-member
from rest_framework import serializers

from . import models

class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Note
    fields = '__all__'
