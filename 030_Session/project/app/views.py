from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        book = {
            'title' : request.POST['title'],
            'publisher' : request.POST['publisher'],
            'author' : request.POST['author'],
        }
        request.session['book'] = book
        request.session.set_expiry(300)  # Expires in 5 minutes
        return redirect('app:results')
    
    return render(request, 'app/index.html')

def results(request):
    context = {
        'book' : request.session['book'],
    }
    return render(request, 'app/results.html', context)

def clear_session(request):
    del request.session['book']
    return redirect('app:index')
