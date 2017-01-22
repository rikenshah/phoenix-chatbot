from __future__ import unicode_literals
from django.contrib.auth.models import UserManager
from django.db import models

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='data')

class KnowledgeBase(models.Model):
	question = models.CharField(max_length = 500)
	answers = models.CharField(max_length = 5000)

	objects = UserManager()