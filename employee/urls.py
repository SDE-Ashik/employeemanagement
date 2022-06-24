from django.urls import path
from employee import views

urlpatterns = [
    path("index", views.IndexView.as_view()),
    # path("login", views.login)
    path("login", views.LoginView.as_view(), name= "login"),
    path("register", views.RegistrationView.as_view(), name ="register"),
    path("profile/add", views.EmployeeCreateView.as_view(), name="emp-add"),
]
