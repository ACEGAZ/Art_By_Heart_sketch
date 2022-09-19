from django.shortcuts import render

# Create your views here.
def index(request):
    """renders index page to index.html """
    return render(request, 'index.html')