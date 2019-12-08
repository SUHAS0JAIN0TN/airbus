from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
        path('',views.index,name='index'),
        path('login/',views.login,name='login'),
        path('signup/',views.signup,name='signup'),
        # path('simp/',views.simp,name='simp')
]