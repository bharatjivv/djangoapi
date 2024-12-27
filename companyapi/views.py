from django.http import HttpResponse

def home_page(request):
    print("home page resquested")
    return HttpResponse("<h1>This is home page </h1>")