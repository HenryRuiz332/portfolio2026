import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from projects.models import Project


class Command(BaseCommand):
    help = 'Importa proyectos desde json/projects.json'

    def handle(self, *args, **options):
        json_path = os.path.join(settings.BASE_DIR, 'json', 'projects.json')

        with open(json_path, 'r', encoding='utf-8') as f:
            categories = json.load(f)

        created = 0
        for category in categories:
            for p in category.get('projects', []):
                project, was_created = Project.all_objects.get_or_create(
                    name=p.get('title', ''),
                    defaults={
                        'description': p.get('description', ''),
                        'technologies': p.get('tecnologies', ''),
                        'company': p.get('company', ''),
                        'status': p.get('status', None),
                    }
                )
                if was_created:
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f'  Creado: {project.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'  Ya existe: {project.name}'))

        self.stdout.write(self.style.SUCCESS(f'\nTotal creados: {created}'))
