from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import datetime
from django.core import serializers

from .forms import AddFishForm
from .models import Fish

# Create your views here.
@login_required
def mapquery(request):
    species = request.GET.get('species')
    fishes = Fish.objects.filter(species=species)
    fishes_json = serializers.serialize('json', fishes)
    response = fishes_json
    return JsonResponse(response, safe=False)

@login_required
def queryfish(request):
    species = request.GET.get('species')
    user = request.user
    fishes = Fish.objects.filter(user=user).filter(species=species)
    fishes_json = serializers.serialize('json', fishes)
    response = fishes_json
    return JsonResponse(response, safe=False)

@login_required
def myprofile(request):
    return render(request, 'profile.html')

@login_required
def addfish(request):
    #If POST request process form data
    if request.method == 'POST':
        form = AddFishForm(request.POST)
        if form.is_valid():
            new_fish = form.save(commit=False)
            new_fish.user = request.user
            new_fish.save()
            return HttpResponseRedirect('/fish/myprofile/')
    else:
        form = AddFishForm()

    return render(request, 'addfish.html', {'form': form})
