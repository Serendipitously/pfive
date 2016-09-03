from django.core.management.base import BaseCommand

import requests

from sync.sessions import GehentaiAPISession

class Command(BaseCommand):
  help = 'Test the Sync Command'

  def handle(self, *args, **options):
    self.stdout.write('Running Ge Sync Command.')
    APISession = GehentaiAPISession()
    response = APISession.post('/',
      json={
        "method": "gdata",
        "gidlist": [
            [449153,"c66e77a80f"]
        ],
        "namespace": 1
      })
    print(response.content)
