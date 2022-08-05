from django.shortcuts import render

class Drum:
  def __init__(self, name, type, description):
    self.name = name
    self.type = type
    self.description = description

drums = [
  Drum('Recording Custom', 'Snare', 'Bright'),
  Drum('Black Beauty', 'Snare', 'Warm and cutting'),
  Drum('Oak Custom', 'Snare', 'Punchy AF'),
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def drums_index(request):
  return render(request, 'drums/index.html', { 'drums': drums })