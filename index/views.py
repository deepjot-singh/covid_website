from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'email' in request.session.keys():
        return render(request, 'index.html', {})
    return redirect('login')