from django.shortcuts import render

# Create your views here.
def intro(request):
  return render(request, 'instructions/intro.html')

def depart(request):
  return render(request, 'instructions/depart.html')

def history(request):
  return render(request, 'instructions/history.html')