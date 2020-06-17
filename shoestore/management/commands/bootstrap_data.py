from django.core.management.base import BaseCommand, CommandError
from shoestore.models import ShoeColor, ShoeType

class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named type arguments
        parser.add_argument(
            '-type', 
            choices = ['sneaker', 'boot', 'sandal', 'dress', 'other'],
            nargs='+', 
            type=str
        )

        # Named color arguments
        parser.add_argument(
            '-color',
            choices = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'white', 'black'],
            nargs='+', 
            type=str
        )

    def handle(self, *args, **kwargs):
        if kwargs['type']:
            for types in kwargs['type']:
                if not types:
                    ShoeType.objects.create(style=types)
                else:
                    raise CommandError('Type "%s" already exists' % types)

        if kwargs['color']:
            for colors in kwargs['color']:
                if not colors:
                    ShoeColor.objects.create(color_name=colors)
                else:
                    raise CommandError('Color "%s" already exists' % colors)
