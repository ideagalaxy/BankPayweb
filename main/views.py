from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware


def cal_exchange(currency):
    exchange_info = Exchange.objects.all().values()[0]

    if currency == "USD":
        rate = exchange_info.dollar2won
    elif currency == "PHP":
        rate = exchange_info.pesso2won
    else:
        rate = exchange_info.yenn2won




def change_money(request):
    print(request.body)
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            user = User.objects.get(username=username)
            pk = user.id
            member = Person.objects.get(person_id = pk)
            if not member.is_manger:
                bankbook = BankBook.objects.get(user_id = member.pk)
                print(bankbook)
        except:
            pass


    return render(request, 'change_money.html')


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
    
    if member.is_manger:
        bankbook = []
    else:
        bankbook = BankBook.objects.get(user_id = member.pk)

    
    context = {"user_detail" : user,
               "bankbook_ifo" : bankbook,
               "member" : member}
    return render(request, 'user_main_page.html',context)




