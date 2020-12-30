from django.shortcuts import render

# Create your views here.

def index(request):
    """
    docstring
    """
    return render(request,'basic_app/index.html')


def other(request):
    """
    docstring
    """
    return render(request,'basic_app/other.html')

def relative(request):
    """
    docstring
    """
    return render(request,'basic_app/relative_url_templates.html')