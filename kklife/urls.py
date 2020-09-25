from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"), 
    path('blogs', views.blogs, name="blogs"),
    path('joinnow', views.joinnow, name="joinnow"),
    path('team', views.team, name="team")
]