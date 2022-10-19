from django.db import models

class Instrument(models.Model):
    """Parent model for a generic 'Instrument' model"""
    about = models.TextField()

# Create your models here.
class MoSAIC(Instrument):
    """Model for the MoSAIC instrument"""
    pass

class CAPE(Instrument):
    """Model for the CAPE instrument"""
    pass

class AETHER(Instrument):
    """Model for the AETHER instrument"""
    pass