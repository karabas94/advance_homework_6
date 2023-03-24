from django.contrib import admin

from .models import Log, People


@admin.register(People)
class PeopleModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name']
    fieldsets = [
        ('People', {'fields': [('first_name', 'last_name'), ]}),
        ('Contact detail', {'fields': ['email'], 'classes': ('collapse',)})
    ]
    list_per_page = 20


@admin.register(Log)
class LogModelAdmin(admin.ModelAdmin):
    list_display = ['path', 'method', 'data', 'timestamp']
    list_filter = ['timestamp']
    search_fields = ['data']
    date_hierarchy = 'timestamp'
    list_per_page = 20
    raw_id_fields = ('user', )
