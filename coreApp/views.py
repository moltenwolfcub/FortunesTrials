from django.shortcuts import render

def index(request):
    """Homepage"""
    return render(request, "coreApp/index.html")
