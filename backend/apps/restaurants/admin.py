from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ['items']  # ✅ use a valid field here

# admin.py
from django.contrib import admin
from .models import Restaurant
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

# Custom form to accept username/email/password
class RestaurantForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    owner_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'address', 'contact', 'is_approved', 'delivery_fees', 'username','owner_name', 'email', 'password','logo']

class RestaurantAdmin(admin.ModelAdmin):
    form = RestaurantForm

    def save_model(self, request, obj, form, change):
        # This method is fine as a fallback, but avoid accessing obj.user here
        super().save_model(request, obj, form, change)

    def save_form(self, request, form, change):
        obj = form.save(commit=False)
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            owner_name=form.cleaned_data['owner_name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        obj.user = user
        obj.save()
        return obj

admin.site.register(Restaurant, RestaurantAdmin)