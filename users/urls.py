from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
        path('',views.index,name='index'),
        path('login/',views.login,name='login'),
        path('signup/',views.signup,name='signup'),
        path('logout/',views.logout_view,name='logout'),
        path('main-page/', views.main_page, name='main_page')
]