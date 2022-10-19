from django.shortcuts import render
from .models import MoSAIC, CAPE, AETHER

# Create your views here.
def mosaic(request):
    """Handles a request for the MoSAIC page"""
    mosaic_bio = MoSAIC.objects.all().first().about if MoSAIC.objects.all().first() else "Work in progress!" 
    return render(request, 'instruments/mosaic.html', {'bio': mosaic_bio})

def aether(request):
    """Handles a request for the AETHER page"""
    aether_bio = AETHER.objects.all().first().about if AETHER.objects.all().first() else "Work in progress!"
    return render(request, 'instruments/aether.html', {'bio': aether_bio})

def cape(request):
    """Handles a request for the CAPE page"""
    cape_bio = CAPE.objects.all().first().about if CAPE.objects.all().first() else "Work in progress!"
    return render(request, 'instruments/cape.html', {'bio': cape_bio})
