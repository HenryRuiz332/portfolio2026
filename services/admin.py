from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon', 'color', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(deleted_at__isnull=True)
