from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render 

from . import predictions
# Create your views here.

def index(request):
    return render(request, "index.html")


def predict(request):
    if request.method == "POST":
        
        Age = float(request.POST.get("age"))
        Fare = float(request.POST.get("fare"))
        Pclass = float(request.POST.get("class"))
        Sex = str(request.POST.get("sex"))
        SibSp = float(request.POST.get("sibsp"))
        Parch = float(request.POST.get("parch"))
        Embarked = str(request.POST.get("embarked"))

        y_pred = predictions.predict([[Age, Fare, Pclass, Sex, SibSp, Parch, Embarked]])

    return HttpResponse(y_pred)





