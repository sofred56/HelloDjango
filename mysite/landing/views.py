from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, welcome in the landing page.")
