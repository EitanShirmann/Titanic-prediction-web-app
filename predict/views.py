from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")


def predict(request):
    if request.method == "POST":
        age = request.json["age"]
        sex = request.POST.get("sex")
        clas = request.json["clas"]
        x = age+clas

    return JsonResponse(x)




