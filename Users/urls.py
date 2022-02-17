from django.urls import path
from Users.views import user_page, get_user_id

urlpatterns = [
    path('page/', user_page, name='user-page'),
    path('page/get/', get_user_id, name='user-page-get')
]
