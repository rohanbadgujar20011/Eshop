from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('signup',views.Signup.as_view(),name="signup"),
    path('feedback',views.feedback,name="feedback"),
    path('login',views.Login.as_view(),name="login")
]