from django.urls import path
from employee import views
urlpatterns = [
    path("index", views.IndexView.as_view()),
    # path("login", views.login)
    path("login", views.LoginView.as_view()),
    path("register", views.RegistrationView.as_view())
]
