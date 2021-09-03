from django.contrib import admin
from myapp.models import Task

# Register your models here.

# admin.site.register(Task)
@admin.register(Task)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'guid',
        'title',
        'description',
        'create_date',
        'uuser',
        
    )
    list_filter = (
        'title',
    )