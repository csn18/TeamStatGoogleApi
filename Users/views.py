import os
import random

from django.shortcuts import render, redirect
from .items import items
from .models import User


def add_users_to_db():
    for user in items:
        User.objects.create(name=user[0], conversion=user[1], ltv=user[2], password=random.randint(10000, 99999))


def get_sheet(request):
    all_users = User.objects.all()
    return render(request, 'main.html', locals())


def get_user_id(request):
    if request.method == 'POST':
        password = request.POST.get('pass-id')
        try:
            user_id = User.objects.get(password=password).id
        except Exception:
            error = 'Введенный код не существует'
            return render(request, 'id.html', locals())
        else:
            return get_user(request, pk=user_id)
    return render(request, 'id.html', locals())


def get_user(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'detail-user.html', locals())


def view_404(request, exception):
    return redirect('id')
