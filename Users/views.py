import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .models import User
from .services import create_or_update_user
from .tasks import get_stats_from_sheet_2, get_stats_from_sheet_1


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
    create_or_update_user(get_stats_from_sheet_1.run())
    create_or_update_user(get_stats_from_sheet_2.run())
    return render(request, 'detail-user.html', locals())


def view_404(request, exception):
    """
    This function work where get error 404 and redirect user to main page
    """
    return redirect('user-page')
