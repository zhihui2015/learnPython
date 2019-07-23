from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(request, "web_javascrip_v0.1.html")
