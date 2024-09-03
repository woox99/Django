from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')


def greet(request, name):
    greeting = request.GET.get('greeting')
    context = {
        'name' : name,
        'greeting' : greeting
    }
    return render(request, 'app/greet.html', context)