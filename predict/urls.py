from django.urls import path, include
from predict.views import predict
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("predict/", views.predict ,name="predict")
]