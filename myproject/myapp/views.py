from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'name': 'Name',
        'age': 21,
    }
    return render(request, 'index.html')

def counter(request):
    text = request.GET['text']
    amount = len(text.split())
    return render(request, 'counter.html', {'amount': amount})