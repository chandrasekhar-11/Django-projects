from django.urls import path
from . import views

urlpatterns = [
    # path('',views.playersea,name="playersea"),
    # path('info/<int:no>/<str:name>',views.func,name="playersea"),
    path('',views.note,name='note'),
    path('',views.create,name='create'),
    path('',views.update,name='update'),
]