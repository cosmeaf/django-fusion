from django.contrib import admin
from .models import Service, OfficePost, Staff


# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'description', 'icon')


@admin.register(OfficePost)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('office', 'created_at', 'updated_at', 'status')


@admin.register(Staff)
class OfficePostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'status')
