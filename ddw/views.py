from django.http import HttpResponse

def title(request):
    return HttpResponse("This is Home Page")
