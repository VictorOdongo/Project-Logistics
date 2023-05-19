from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def getstarted_view(request):
    return render(request, 'user/getstarted.html')

def personal_view(request):
    return render(request, 'user/personal-signup.html')
