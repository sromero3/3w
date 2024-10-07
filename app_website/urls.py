from unicodedata import name
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
#from app_website.forms import LoginForm

#  Urls del website
urlpatterns = [
   path("", include("app_gestion.urls")) 

    #path('accounts/login/', auth_views.LoginView.as_view(
    #     authentication_form=LoginForm,
    #     ), name="login"),
]

# handler404 = 'app_website.views.Error404View' 

# handler500 = 'app_website.views.Error500View' 