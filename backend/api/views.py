import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    print(request.GET)  # urls query params
    print(request.POST)
    body = request.body  # byte string JSON data
    data = {}
    try:
        data = json.loads(body)  # JSON string data -> Python Dictionary
    except:
        pass
    print(data)
    # data['headers'] = request.headers
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
