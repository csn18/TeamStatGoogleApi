from django.contrib import admin

from Users.models import User, Curator


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'curator', 'password', 'conversion', 'ltv', 'remaining']
    search_fields = ['name']
    list_filter = ['curator']


admin.site.register(Curator)
