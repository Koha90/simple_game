from django.contrib import admin
from .models import Profile, Cartridge


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


@admin.register(Cartridge)
class PostAdmin(admin.ModelAdmin):
    list_display = ('address', 'date_repairs', 'total', 'status', 'client')
    list_filter = ('status', 'address', 'date_repairs',)
    search_fields = ('address', 'client')
    ordering = ('status',)