from django.shortcuts import render, redirect 


def index(request):
    return render(request, 'intro.html', status=200)


def handle_login_view(request):
    pass 


def login_manage_view(request):
    pass 


def login_staff_view(request):
    pass 


def logout_view(request):
    pass 



