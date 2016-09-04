from django.core.management.base import BaseCommand

import requests

from sync.sessions import GehentaiAPISession

class Command(BaseCommand):
  help = 'Test the Ge Sync Command'

  def handle(self, *args, **options):
    self.stdout.write('Running Ge Sync Command.')
    APISession = GehentaiAPISession()
    response = APISession.post('/',
      json={
        "method": "gdata",
        "gidlist": [
            [972589, "61204a23cf"]
        ],
        "namespace": 1
      })
    print(response.content)
