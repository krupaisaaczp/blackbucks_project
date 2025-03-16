from django.contrib import admin
from .models import AdminPanel

class AdminPanelAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Customize display fields in the admin panel

admin.site.register(AdminPanel, AdminPanelAdmin)
