from django.shortcuts import render
from . forms import ExampleForm

# Create your views here.

def DjangoForm(request):
    form = ExampleForm
    return render(request, 'django_forms.html', {'form' : form})