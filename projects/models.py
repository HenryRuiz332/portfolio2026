import os
from django.db import models
from config.timestamps import Timestamp
from django.utils import timezone
from django.utils.text import slugify

class ProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class Project(Timestamp):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)

    objects = ProjectManager()
    all_objects = models.Manager()

    def delete(self, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_name = None
        if not is_new:
            old_instance = Project.all_objects.get(pk=self.pk)
            old_name = old_instance.name
        
        super().save(*args, **kwargs)
        
        # Si el nombre cambió, actualizamos las URLs de las imágenes asociadas
        if not is_new and old_name != self.name:
            for img in self.images.all():
                img.save() # Esto disparará la actualización de su campo url

    def __str__(self):
        return self.name

def project_image_path(instance, filename):
    ext = filename.split('.')[-1]
    # Usamos el nombre actual del proyecto
    project_name = instance.project.name if instance.project and instance.project.name else "project"
    name = slugify(project_name)
    
    # Buscamos el siguiente número disponible para este proyecto
    # Si la instancia ya tiene un ID, no contamos a sí misma si ya tiene imagen
    # Pero para simplificar y asegurar unicidad, usamos el count total + 1
    count = ProjectImage.all_objects.filter(project=instance.project).count() + 1
    filename = f"{name}-{count}.{ext}"
    
    return os.path.join('public/images/projects/', filename)

class ProjectImage(Timestamp):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=project_image_path)
    url = models.CharField(max_length=500, null=True, blank=True)

    objects = ProjectManager()
    all_objects = models.Manager()

    def save(self, *args, **kwargs):
        # Guardamos primero para asegurar que el archivo esté en disco y tenga nombre
        super().save(*args, **kwargs)
        
        if self.image:
            from django.conf import settings
            relative_path = self.image.name
            full_url = f"{settings.STATIC_URL}{relative_path}"
            
            # Solo actualizamos si la URL guardada es diferente a la calculada
            if self.url != full_url:
                self.url = full_url
                # Usamos update para evitar recursión infinita de save()
                ProjectImage.all_objects.filter(id=self.id).update(url=full_url)

    def __str__(self):
        return f"Image for {self.project.name}"
