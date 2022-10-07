from django.db import models

# Create your models here.
class SCUPBio(models.Model):
    """Model for the homepage bio content"""
    content = models.TextField()