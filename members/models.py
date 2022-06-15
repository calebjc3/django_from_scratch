from django.db import models

class Member(models.Model):
  message = models.CharField(max_length=200)

