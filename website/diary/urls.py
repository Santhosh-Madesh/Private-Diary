from django.urls import path
from . import views
from . import auth

urlpatterns=[
    path("",views.index,name="index"),
    path("create/",views.write_diary,name="create"),
    path("signup/",auth.signup,name="signup"),
    path("login/",auth.login_page,name="login"),
    path("change_password/",auth.change_password,name="change_password"),
    path("logout/",auth.logout_page,name="logout"),
    path("dashboard/",views.personal_dashboard,name="dashboard"),
    path("update_dashboard/",views.update_dashboard,name="update_dashboard"),
]