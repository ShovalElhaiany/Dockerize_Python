from django.urls import path, include
from . import views

app_name = "pydockapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('newthing/', views.newthing, name="newthing"),
]
