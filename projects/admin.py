from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class DeletedListFilter(admin.SimpleListFilter):
    title = 'Papelera'
    parameter_name = 'deleted'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'En papelera'),
            ('no', 'Activos'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return Project.all_objects.filter(deleted_at__isnull=False)
        if self.value() == 'no':
            return queryset.filter(deleted_at__isnull=True)
        return queryset

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'deleted_at')
    search_fields = ('name', 'description')
    list_filter = (DeletedListFilter,)
    inlines = [ProjectImageInline]
    actions = ['restore_projects']

    def get_queryset(self, request):
        # Permitimos ver todos en el admin para que el filtro de papelera funcione
        return Project.all_objects.all()

    def restore_projects(self, request, queryset):
        queryset.update(deleted_at=None)
    restore_projects.short_description = "Restaurar proyectos seleccionados"
