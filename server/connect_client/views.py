import json
from django.http import HttpResponse

# Register your models here.

def index(request):
    data = {'connected': True}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')