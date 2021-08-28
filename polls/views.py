from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from polls.forms import AddPerson
from polls.models import Person


def index(request):
    if request.method == "GET":
        form = AddPerson()
    else:
        form = AddPerson(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("запись создана")

    return render(request, "polls/index.html", context={"form": form})


def person_id(request, p_id):
    obj = get_object_or_404(Person, pk=p_id)
    form = AddPerson(instance=obj)
    if request.method == 'POST':
        form = AddPerson(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные сохранены')
    data = {'form': form}
    return render(request, 'polls/index.html', context=data)
