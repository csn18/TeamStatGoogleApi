import json
import random

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .models import User
from .tasks import get_stats_from_sheet_2, get_stats_from_sheet_1


def add_users_from_other_table():
    users = []
    for user in users:
        User.objects.create(
            name=user[0],
            conversion=user[1],
            ltv=user[2],
            password=random.randint(1000, 9999)
        )


def add_users_to_db():
    users = []
    for user in users:
        User.objects.create(
            name=user[0],
            conversion=user[1],
            ltv=user[2],
            password=random.randint(10000, 99999)
        )


def get_user_id(request):
    """
    This function get user id from request and return JSON with user data
    """
    if request.method == 'GET':
        password = request.GET.get('user-id')
        try:
            user = User.objects.get(password=password)
            data = {
                'name': str(str(user.name).split().pop(1)),
                'ltv': user.ltv, 'conversion': user.conversion,
                'reminder': user.remaining
            }
            return HttpResponse(json.dumps(data), content_type="application/json")
        except Exception:
            error = 'Введенный код не существует'
            return JsonResponse({'error': error})


def user_page(request):
    """
    This function render page with input field for get user id
    """
    get_stats_from_sheet_1.apply()
    get_stats_from_sheet_2.apply()
    return render(request, 'detail-user.html', locals())


def view_404(request, exception):
    """
    This function work where get error 404 and redirect user to main page
    """
    return redirect('user-page')
