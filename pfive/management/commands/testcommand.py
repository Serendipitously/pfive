from django.core.management.base import BaseCommand

import requests


class Command(BaseCommand):
  help = 'Main test command'

  def handle(self, *args, **options):
    self.stdout.write('Running main test command')

    response = requests.get('http://www.google.com')
    print(response.data)
