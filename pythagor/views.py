from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PeopleForm, Pythagor
from .models import People


def index(request):
    return render(request, 'pythagor/index.html')


def hypotenuse(request):
    side_c = request.GET.get('side_c', '')
    return render(request, 'pythagor/hypotenuse.html', {'side_c': side_c})


def triangle(request):
    if "ok" in request.GET:
        triangle_form = Pythagor(request.GET)
        if triangle_form.is_valid():
            side_a = triangle_form.cleaned_data['side_a']
            side_b = triangle_form.cleaned_data['side_b']
            side_c = (side_a ** 2 + side_b ** 2) ** 0.5
            redirect_url = reverse('pythagor:hypotenuse') + f'?side_c={side_c}'
            return HttpResponseRedirect(redirect_url)
    else:
        triangle_form = Pythagor()
    return render(request, 'pythagor/triangle.html', {'triangle_form': triangle_form})


def contact_form_detail(request, pk):
    obj = get_object_or_404(People, pk=pk)
    return render(request, 'pythagor/people-detail.html', {'obj': obj})


def contact_form(request):
    if request.method == 'POST':
        user_form = PeopleForm(request.POST)
        if user_form.is_valid():
            obj = user_form.save()
            return redirect('pythagor:people_detail', pk=obj.pk)
    else:
        user_form = PeopleForm()
    return render(request, 'pythagor/people.html', {'user_form': user_form})


def contact_form_result(request):
    user = People.objects.all()
    return render(request, 'pythagor/people-result.html', {"user": user})


def contact_form_edit(request, pk):
    obj = get_object_or_404(People, pk=pk)
    if request.method == 'POST':
        user_form = PeopleForm(request.POST, instance=obj)
        if user_form.is_valid():
            obj = user_form.save()
            return redirect('pythagor:people_detail', pk=obj.pk)
    else:
        user_form = PeopleForm(instance=obj)
    return render(request, 'pythagor/people-edit.html', {'user_form': user_form, 'obj': obj})


def contact_form_delete(request, pk):
    obj = get_object_or_404(People, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('pythagor:result')
    return render(request, 'pythagor/people-delete.html', {'obj': obj})
