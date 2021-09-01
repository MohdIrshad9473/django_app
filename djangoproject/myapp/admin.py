from django.contrib import admin
from myapp.models import Task

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, AuthorAdmin)

