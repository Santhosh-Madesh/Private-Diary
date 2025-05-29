from django.urls import path
from . import views
from . import auth

urlpatterns=[
    path("",views.index,name="index"),
    path("create/",views.write_diary,name="create"),
    path("signup/",auth.signup,name="signup"),
    path("login/",auth.login_page,name="login"),
]