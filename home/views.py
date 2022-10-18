from django.shortcuts import render
from .models import SCUPBio, MoSAICBio, AETHERBio, CAPEBio

# Create your views here.
def index(request):
    """Handles the main SCUP homepage"""
    scup_bio = SCUPBIO.objects.all().first().content if SCUPBio.objects.all().first() else "Work in progress!"
    mosaic_bio = MoSAICBio.objects.all().first().content if MoSAICBio.objects.all().first() else "Work in progress!"
    aether_bio = AETHERBio.objects.all().first().content if AETHERBio.objects.all().first() else "Work in progress!"
    cape_bio = CAPEBio.objects.all().first().content if CAPEBio.objects.all().first() else "Work in progress!"
    return render(request, 'home/index.html', {"top_bio": scup_bio, "mosaic_bio": mosaic_bio, "aether_bio": aether_bio, "cape_bio": cape_bio})