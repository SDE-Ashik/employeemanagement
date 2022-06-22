from django.urls import path
from mathcalculation import views

urlpatterns = [
    path("sum", views.AddView.as_view()),
    path("sub", views.SubView.as_view()),
    path("mul", views.MulView.as_view()),
    path("div",views.DiviForm.as_view()),
]