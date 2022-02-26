from django.shortcuts import render
from computer.models import Computer
from computer.models import Disk
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound


def index(request):
    comp = Computer.objects.all()
    disk = Disk.objects.all()
    return render(request, "main.html", {"comps": comp, "disks": disk})


def createComp(request):
    if request.method == "POST":
        comp = Computer()
        comp.name = request.POST.get("name")
        comp.save()
    return render(request, 'createComp.html')

def createDi(request):
    if request.method == "POST":
        di = Disk()
        di.name = request.POST.get("name")
        di.cost = request.POST.get("cost")
        di.computer_id = Computer.objects.get(name=request.POST.get("computer_id"))
        di.save()
    return render(request, 'createDi.html')

def deleteComp(request, id):
    try:
        comp = Computer.objects.get(id=id)
        comp.delete()
        return HttpResponseRedirect("/")
    except Computer.DoesNotExist:
        return HttpResponseNotFound("<h2>Не найдено</h2>")

def deleteDi(request, id):
    try:
        di = Disk.objects.get(id=id)
        di.delete()
        return HttpResponseRedirect("/")
    except Disk.DoesNotExist:
        return HttpResponseNotFound("<h2>Не найдено</h2>")

def editComp(request, id):
    try:
        comp = Computer.objects.get(id=id)
        if request.method == "POST":
            comp.name = request.POST.get("name")
            comp.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "editComp.html", {"comp":comp})
    except Computer.DoesNotExist:
        return HttpResponseNotFound("<h2>Не найдено</h2>")

def editDi(request, id):
    try:
        di = Disk.objects.get(id=id)
        if request.method == "POST":
            di.name = request.POST.get("name")
            di.cost = request.POST.get("cost")
            di.computer_id = Computer.objects.get(name=request.POST.get("computer_id"))
            di.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "editDi.html", {"di":di})
    except Disk.DoesNotExist:
        return HttpResponseNotFound("<h2>Не найдено</h2>")
