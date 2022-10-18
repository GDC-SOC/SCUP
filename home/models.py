from django.db import models

# Create your models here.
class SCUPBio(models.Model):
    """Model for the homepage bio content"""
    content = models.TextField()

class MoSAICBio(models.Model):
    """Model for the MoSAIC bio on the homepage"""
    content = models.TextField()

class AETHERBio(models.Model):
    """Model for the AETHER bio on the homepage"""
    content = models.TextField()

class CAPEBio(models.Model):
    """Model for the CAPE bio on the homepage"""
    content = models.TextField()