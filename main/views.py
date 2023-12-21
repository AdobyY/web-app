from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 20,
            'hobby': 'gym'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')