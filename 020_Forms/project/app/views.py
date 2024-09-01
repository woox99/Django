from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        context = {
            'title' : request.POST['title'],
            'publisher' : request.POST['publisher'],
            'author' : request.POST['author']
        }
        print(context)
        return redirect('app:confirmation')
    return render(request, 'app/index.html')
    
def confirmation(request):
    return render(request, 'app/confirmation.html')    
