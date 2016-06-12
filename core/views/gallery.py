from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from core.models import Gallery
from core.serializers import GallerySerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def gallery_list(request):
    """
    List all code snippets, or create a new gallery.
    """
    if request.method == 'GET':
        snippets = Gallery.objects.all()
        serializer = GallerySerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GallerySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def gallery_detail(request, pk):
    """
    Retrieve, update or delete a code gallery.
    """
    try:
        gallery = Gallery.objects.get(pk=pk)
    except Gallery.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GallerySerializer(gallery)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GallerySerializer(gallery, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        gallery.delete()
        return HttpResponse(status=204)
