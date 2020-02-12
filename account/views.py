from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authinticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('exam:exam'))

    return render(request, 'account/login.html')


def register(request):

    return render(request, 'account/register.html')
