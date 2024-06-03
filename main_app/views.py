from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

finches = [
  {'name': 'Red', 'breed': 'Red Crossbill', 'description': 'red feathers with dark brown wings', 'age': 3},
  {'name': 'Rosy', 'breed': 'Black Rosy-Finch', 'description': 'brown and white with pink accent', 'age': 2},
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/{id}'

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'