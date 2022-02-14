from django.urls import path

from Users.views import get_sheet, get_user, get_user_id

urlpatterns = [
    path('', get_user_id, name='id'),
]
