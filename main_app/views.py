from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class DrumCreate(CreateView):
  model = Drum
  fields = '__all__'
  success_url = '/drums/'

class DrumUpdate(UpdateView):
  model = Drum
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['type', 'description']

class DrumDelete(DeleteView):
  model = Drum
  success_url = '/drums/'