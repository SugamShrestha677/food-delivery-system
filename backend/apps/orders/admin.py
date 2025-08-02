from django.contrib import admin
from django import forms
from .models import Order,OrderItem
from apps.accounts.models import Users

class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderAdminForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Users.objects.filter(role='customer')  # Adjust based on your field name

class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)