from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import Pythagor


def hypotenuse(request):
    side_c = request.GET.get('side_c', '')
    return render(request, 'pythagor/hypotenuse.html', {'side_c': side_c})


def index(request):
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
    return render(request, 'pythagor/index.html', {'triangle_form': triangle_form})
