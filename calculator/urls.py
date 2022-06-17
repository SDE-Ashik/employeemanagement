from django.urls import path
from calculator import views

urlpatterns = [
    path("home", views.HomeView.as_view()),
    path("add", views.AddView.as_view()),
    path("sub", views.SubView.as_view()),
    path("mul", views.MulView.as_view()),
    path("div", views.DivView.as_view()),
    path("cube", views.CubeView.as_view()),
    path("square", views.SquareView.as_view()),
    path("factorial", views.FactView.as_view()),
    path("wordcount", views.CountView.as_view()),
    path("prime",views.PrimeView.as_view()),

]
