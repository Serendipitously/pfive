from django.core.management.base import BaseCommand

import requests


class Command(BaseCommand):
  help = 'Test the Sync Command'

  def handle(self, *args, **options):
    self.stdout.write('Running Sync Command.')

    response = requests.get('http://www.google.com')
    print(response.content)
