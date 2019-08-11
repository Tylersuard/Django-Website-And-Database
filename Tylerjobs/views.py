from django.shortcuts import render
from .models import Job


def meez(request):
    jobs = Job.objects 
    return render(request,'Tylerjobs/meez.html', {'jobs':jobs})
# Create your views here.
