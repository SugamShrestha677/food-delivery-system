from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

class CustomUserAdmin(UserAdmin):
    model = Users

    # Fields to display in the list view
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

    # Fieldsets for change view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'address', 'photo')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields for the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'phone', 'address', 'photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(Users, CustomUserAdmin)


# from django.contrib.auth.admin import UserAdmin
# Register your models here.
# admin.site.register(Users)
# users/admin.py