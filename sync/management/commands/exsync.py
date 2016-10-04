from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup

from sync.sessions import GehentaiAPISession, GehentaiSession


# [449153, "c66e77a80f"],
# [972361, "93ef78bd66"],
# [972366, "fd27efe48b"],
# [972384, "a2f2f34b98"],
# [972376, "cdd3f04f55"],
# [972380, "e67133b172"],
# [972341, "2609e79f73"],
# [972358, "9581c72fea"]

class Command(BaseCommand):
  help = 'Test the Ex Sync Command'


  def add_arguments(self, parser):
    parser.add_argument('page', type=int)


  def handle(self, *args, **options):
    self.stdout.write('Running Ex Sync Command.')

    APISession = GehentaiAPISession()
    # response = APISession.post('/',
    #   json={
    #     "method": "gdata",
    #     "gidlist": [
    #       [449153, "c66e77a80f"]
    #     ],
    #     "namespace": 1
    #   })
    # print(response.content)

    session = GehentaiSession()
    page = options.get('page', None)
    response = session.getList(page=page)
    # print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all('div', class_='it5')
    links = [element.a['href'] for element in divs]
    print(len(links))

    print(links)
