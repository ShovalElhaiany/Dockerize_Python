from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Thing


def index(request):
    things = Thing.objects.all()
    return render(request=request, template_name="things.html", context={"things":things})

def newthing(request):
    if request.method=="POST":
        name = request.POST['name']
        age = request.POST['age']
        thing = Thing(name=name, age=age)
        thing.save()
        return HttpResponseRedirect(reverse('pydockapp:index'))
    else:
        return render(request=request, template_name="addthing.html")
