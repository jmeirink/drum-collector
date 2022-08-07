from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Drum, Accessory
from .forms import MaintenanceForm

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
  maintenance_form = MaintenanceForm()
  return render(request, 'drums/detail.html', {
    'drum': drum, 'maintenance_form': maintenance_form
  })

def add_maintenance(request, drum_id):
  # create a ModelForm instance using the data in request.POST
  form = MaintenanceForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the drum_id assigned
    new_maintenance = form.save(commit=False)

    new_maintenance.drum_id = drum_id
    new_maintenance.save()
  return redirect('drums_detail', drum_id=drum_id)

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

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'use']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'