from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Drum, Accessory
from .forms import MaintenanceForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def drums_index(request):
  drums = Drum.objects.filter(user=request.user)
  return render(request, 'drums/index.html', { 'drums': drums })

@login_required
def drums_detail(request, drum_id):
  drum = Drum.objects.get(id=drum_id)
  maintenance_form = MaintenanceForm()
  return render(request, 'drums/detail.html', {
    'drum': drum, 'maintenance_form': maintenance_form
  })

@login_required
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

class DrumCreate(LoginRequiredMixin, CreateView):
  model = Drum
  fields = '__all__'
  success_url = '/drums/'

  # This inherited method is called when a
  # valid drum form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the drum
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class DrumUpdate(LoginRequiredMixin, UpdateView):
  model = Drum
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['type', 'description']

class DrumDelete(LoginRequiredMixin, DeleteView):
  model = Drum
  success_url = '/drums/'

class AccessoryCreate(LoginRequiredMixin, CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryList(LoginRequiredMixin, ListView):
  model = Accessory

class AccessoryDetail(LoginRequiredMixin, DetailView):
  model = Accessory

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
  model = Accessory
  fields = ['name', 'use']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
  model = Accessory
  success_url = '/accessories/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('drums_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
