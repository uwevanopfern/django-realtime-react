# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=no-member
from django.db import models

class Note(models.Model):
  title = models.CharField(max_length=150)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title 
