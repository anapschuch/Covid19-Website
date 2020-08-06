from django.shortcuts import render

def home(request):
    '''
    From url: r'^$'
    Description: First view called when opening the site. Returns a template for
    home page.
    '''
    return render(request, 'home.html')
