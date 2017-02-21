from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, entry_id):
    response = "You are looking at the detail of entry %s."
    return HttpResponse(response % entry_id)
