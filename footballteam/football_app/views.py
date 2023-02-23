from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TeamForm
from .models import Team


# Create your views here.
def index(request):
    team = Team.objects.all()
    context = {
        'team_details': team
    }
    return render(request, 'index.html', context)


def single(request, team_id):
    team = Team.objects.get(id=team_id)
    return render(request, 'details.html', {'team': team})


def add_team(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rank = request.POST.get('rank')
        point = request.POST.get('point')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        team = Team(name=name, rank=rank, point=point, desc=desc, img=img)
        team.save()
    return render(request, 'add_team.html')


def update(request, id):
    team = Team.objects.get(id=id)
    form = TeamForm(request.POST or None, request.FILES, instance=team)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'team': team})


def delete(request, id):
    if request.method=='POST':
        team = Team.objects.get(id=id)
        team.delete()
        return redirect('/')
    return render(request,'delete.html')