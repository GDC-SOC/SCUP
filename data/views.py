from django.shortcuts import render

# Create your views here.
async def index(request):
    """Handles the SCUP data page"""

    return render(request, 'data/index.html')