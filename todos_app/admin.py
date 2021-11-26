from django.contrib import admin
from todos_app.models import Task

class Tasks(admin.ModelAdmin):
    list_display = ('id','status', 'name', 'description')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'description')
    list_per_page = 20


admin.site.register(Task, Tasks)