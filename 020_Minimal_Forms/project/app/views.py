from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        context = {
            'title' : request.POST['title'],
            'publisher' : request.POST['publisher'],
            'author' : request.POST['author']
        }
        return render(request, 'app/book_view.html', context) # You would not normally render a page after handling a form
    return render(request, 'app/index.html')
