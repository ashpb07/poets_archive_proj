from django.urls import path
from . import views
urlpatterns = [
     path('', views.home, name='home'),
     path('signup/', views.signup, name='signup'), 
     path('signin/', views.signin, name='signin'),  
     path('about/',views.about,name='about'),
     path('collections/',views.collection,name='collection'),
     path('profile/',views.profile,name='profile'),
     path('signout/',views.signout,name='signout'),
     path('member/',views.member,name="member"),
      path('publish/',views.publish,name="publish"),
       path('learn/',views.learn,name="learn"),
      #path('accounts/login/',views.signin, name='login'),

]

