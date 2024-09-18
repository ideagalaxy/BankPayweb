from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware

def first_page(request):
    print("this is first_page")
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "log_in":
            print(action)
            return redirect('/log_in')

    return render(request, 'first_page.html')

def login_page(request):
    print("this is login_page")
    print(request)

    if request.method == "POST":
        userid = request.POST.get("username")
        pwd = request.POST.get("password")
        print(userid)
        print(pwd)
        user = auth.authenticate(request, username = userid, password = pwd)
        print(user)
        user = User.objects.get(username = userid)
        print(user.is_active)

        if user is not None:
            auth.login(request, user)
            print(user.pk)
            return redirect(f'/{user.pk}/')


    return render(request, 'login_page.html')

def exchange_rate(request):
    exchange_info = Exchange.objects.all().values()[0]
    user_pk = request.user.pk
    user = User.objects.get(id=user_pk)
    context = {'info' : exchange_info,
               'user' : user}
    return render(request, 'exchange.html',context)


def user_main_page(request, pk):
    user = User.objects.get(id=pk)
    member = Person.objects.get(person_id = pk)
    bankbook = BankBook.objects.get(user_id = member.pk)
    context = {"user_detail" : user,
               "bankbook_ifo" : bankbook}
    return render(request, 'user_main_page.html',context)




