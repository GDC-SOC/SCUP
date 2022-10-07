from django.shortcuts import render
from .models import SCUPBio

# Create your views here.
def index(request):
    """Handles the main SCUP homepage"""
    return render(request, 'home/index.html', {"top_bio": SCUPBio.objects.all().first().content})