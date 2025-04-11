from django.shortcuts import render, redirect
from django.views import View
from .models import Fest, Mig, Members, Anmeld 
from .forms import FestForm, AnmeldForm 

# Create your views here.
class Index(View):
  def get(self, request, *args, **kwargs):
    mig = Mig.objects.all()
    members = Members.objects.all().values()
    fes= Fest.objects.all()
    fest = Fest.objects.all()
    form = FestForm()
    form1 = AnmeldForm()
    anmeld=Anmeld.objects.all()
    anm = Anmeld.objects.all ()
    context = {
      'mig': mig,
      'members': members,
      'fes': fes,
      'fest': fest,
      'form': form,
      'anmeld': anmeld,
      'form1': form1,
      'anm': anm,
      
    }
    return render(request, 'lys/base.html', context)

  def post(self, request, *args, **kwargs):
    form = FestForm(request.POST)
    form1 = AnmeldForm(request.POST)
    if form.is_valid():
        form.save()
        
        return redirect('/')
    if form1.is_valid():
        form1.save()
        return redirect('/')
    
    fest = Fest.objects.all()
    anmeld = Anmeld.objects.all()
    context = {
        'fest': fest, 
        'form': form,
        'anmeld': anmeld,
        'form1': form1,
    }
    return render(request, 'lys/base.html', context)
    
  