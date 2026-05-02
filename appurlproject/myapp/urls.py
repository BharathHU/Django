from django.urls import path
from myapp.views import home
urlpatterns={
    path('r1/',home)
}