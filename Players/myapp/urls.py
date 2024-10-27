# player_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.playersea,name="playersea"),
    # path('info/<int:no>/<str:name>',views.func,name="playersea"),
    # path('',views.playersear,name="player"),
    # path('',views.Usersview,name="users"),
    path('',views.loginview,name="users"),
]
