from django.core.management.base import BaseCommand
from taskAPI_base.models import Category, SubCategory


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Category.objects.count() == 0:
            Category.objects.create(description='status')

        if SubCategory.objects.count() == 0:
            c = Category.objects.get(description='status')         
            SubCategory.objects.create(description="A Realizar", category=c)
            SubCategory.objects.create(description="Em Andamento", category=c)
            SubCategory.objects.create(description="Concluído", category=c)