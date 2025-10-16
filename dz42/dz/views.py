from django.http import HttpResponse

def hello(request):
    return HttpResponse("Привет! Это строка из Django.")
