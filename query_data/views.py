from django.shortcuts import render

# Create your views here.
def query_home (request):
    return render(request, 'query_home.html')
