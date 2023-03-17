from django.shortcuts import redirect, render, HttpResponse
from .forms import Pythagor


def hypotenuse(request):
    side_c = request.session.get('side_c', None)
    return render(request, 'pythagor/hypotenuse.html', {'side_c': side_c})


def index(request):
    side_a = None
    side_b = None
    if "ok" in request.GET:
        triangle_form = Pythagor(request.GET)
        if triangle_form.is_valid():
            side_a = triangle_form.cleaned_data['side_a']
            side_b = triangle_form.cleaned_data['side_b']
            side_c = (side_a ** 2 + side_b ** 2)
            request.session['side_c'] = side_c
        return redirect('pythagor:hypotenuse')
    else:
        triangle_form = Pythagor()
    return render(request, 'pythagor/index.html', {'side_a': side_a, 'side_b': side_b, 'triangle_form': triangle_form})
