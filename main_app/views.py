from django.shortcuts import render
from .models import Drum

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def drums_index(request):
  drums = Drum.objects.all()
  return render(request, 'drums/index.html', { 'drums': drums })

def drums_detail(request, drum_id):
  drum = Drum.objects.get(id=drum_id)
  return render(request, 'drums/detail.html', { 'drum': drum })