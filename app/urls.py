from django.urls import path

from app import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('addpage',views.addpage,name='addpage'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('delete/<int:id>',views.deletpost,name='delete'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
