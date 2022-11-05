from django.urls import path
from game import views

urlpatterns = [
   path('startgame/', views.startgame),
   path('getBoard/<id>', views.getBoard),
   path('getGames/', views.getGames),
   path('updateBoard/<id>', views.updateBoard),

]