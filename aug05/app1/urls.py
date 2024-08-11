from django.urls import path
from app1 import views 


urlpatterns=[
    path('',views.home,name="homepage"),
    path('login',views.loginV,name="loginpage"),
    path('profile',views.profile,name="profilepage"),
    path('logout',views.logoutV,name="logoutpage"),
    path('register',views.register,name="registerpage"),
    path('create',views.tweetView,name='createpost'),
    path('delete/<int:rid>',views.deleteView,name='deletepost'),
    path('display/<int:rid>',views.display,name='showPost'),
    # path('tweet/<int:tweet_id>/react/', views.add_reaction, name='add_reaction'),
    # path('', views.tweet_list, name='tweet_list'),
    # path('tweet/<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),

]