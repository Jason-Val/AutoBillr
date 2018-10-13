from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def about(request):
    #returns html for the about page
    return render(request, 'about.html')

def db(request):

    return render(request, 'db.html', {})