from django.urls import path
from calculator import views

urlpatterns = [
    path("home", views.HomeView.as_view(),name ="cal-home"),
    path("add", views.AddView.as_view() , name = "cal-add"),
    path("sub", views.SubView.as_view(), name ="cal-sub"),
    path("mul", views.MulView.as_view(),name ="cal-mul"),
    path("div", views.DivView.as_view(), name ="cal-div"),
    path("cube", views.CubeView.as_view(), name ="cal-cube"),
    path("square", views.SquareView.as_view(), name ="cal-square"),
    path("factorial", views.FactView.as_view(), name ="cal-factorial"),
    path("wordcount", views.CountView.as_view(),name ="cal-wordcount"),
    path("prime",views.PrimeView.as_view(),name ="cal-prime"),

]
