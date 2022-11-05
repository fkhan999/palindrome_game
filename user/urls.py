from django.urls import path
from user import views

urlpatterns = [
    #path('', views.home),
    path('createUser/', views.createUser),
    path('deleteUser/', views.deleteUser),
    path('updateUser/', views.updateUser),

]