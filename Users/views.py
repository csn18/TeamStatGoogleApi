import json
import random

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .items import users
from .models import User


def add_users_to_db():
    for user in users:
        User.objects.create(
            name=user[0],
            conversion=user[1],
            ltv=user[2],
            password=random.randint(10000, 99999)
        )


def update_users_data():
    for user_object in users:
        user_db = User.objects.get(name=user_object[0])
        user_db.remaining = 0 if user_object[3] <= 0 else user_object[3]
        user_db.save()


def get_sheet(request):
    all_users = User.objects.all()
    return render(request, 'main.html', locals())


def get_user_id(request):
    if request.method == 'GET':
        password = request.GET.get('user-id')
        try:
            user = User.objects.get(password=password)
            data = {'name': str(str(user.name).split().pop(1)), 'ltv': user.ltv, 'conversion': user.conversion,
                    'reminder': user.remaining}
            return HttpResponse(json.dumps(data), content_type="application/json")
        except Exception:
            error = 'Введенный код не существует'
            return JsonResponse({'error': error})


def user_page(request):
    return render(request, 'detail-user.html', locals())


def view_404(request, exception):
    return redirect('user-page')
