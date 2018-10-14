from django.shortcuts import render
from django.http import HttpResponse

from .forms import BillCreationForm
# Create your views here.
def getBill(request):
    if(request.method == 'POST'):
        form = BillCreationForm(request.POST)
        if(form.is_valid()):
            return HttpResponseRedirect('/addmember/')
    else:
        form = NameForm()

    return render(request, 'profile.html', {'form': form})

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def db(request):

    return render(request, 'db.html', {})
