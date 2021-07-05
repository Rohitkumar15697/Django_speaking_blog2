
from django.urls import path,include
from .import views
from homeapp.views import search_result 

urlpatterns = [

    path('profile/',views.profile,name='profile'),
    path('logout/',views.logoutme,name='logout'),
    path('search/',search_result),

]