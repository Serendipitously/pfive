from django.core.management.base import BaseCommand

from sync.sessions import GehentaiAPISession


# [449153, "c66e77a80f"],
# [972361, "93ef78bd66"],
# [972366, "fd27efe48b"],
# [972384, "a2f2f34b98"],
# [972376, "cdd3f04f55"],
# [972380, "e67133b172"],
# [972341, "2609e79f73"],
# [972358, "9581c72fea"]

class Command(BaseCommand):
  help = 'Test the Sync Command'

  def handle(self, *args, **options):
    self.stdout.write('Running Ex Sync Command.')

    APISession = GehentaiAPISession()
    response = APISession.post('/',
      json={
        "method": "gdata",
        "gidlist": [
          [449153, "c66e77a80f"]
        ],
        "namespace": 1
      })
    print(response.content)
