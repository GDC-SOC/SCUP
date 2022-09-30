from django.shortcuts import render

SCUP_HOMEPAGE_TOP_BIO = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sagittis efficitur nunc, sed tincidunt ligula efficitur sed. Duis a dolor sit amet enim venenatis pulvinar. Nunc semper pretium leo, eget aliquet lorem fringilla ac. Curabitur euismod vel erat et lobortis. Nulla varius varius orci, eu venenatis massa ullamcorper ut. Cras quam est, tristique sed tempus sit amet, scelerisque at justo. Maecenas eleifend nibh sodales, consequat tellus eu, cursus quam. Morbi sit amet accumsan ipsum, eget tempus nulla. 
"""

# Create your views here.
def index(request):
    """Handles the main SCUP homepage"""
    return render(request, 'home/index.html', {"top_bio": SCUP_HOMEPAGE_TOP_BIO})