from django.shortcuts import render

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
  return render(request, 'finches/index.html', {
    'finches': finches
  })