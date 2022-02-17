from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
]

handler404 = 'Users.views.view_404'
