from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('home/',views.dashboard_view,name='home'),
    path('userpresent/',views.user_present,name='userpresent'),
    path('logout/',views.logout_view,name='logout'),
    
]
