from django.urls import path, include
import football_app
from football_app import views

app_name = 'football_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('team/<int:team_id>', views.single, name='single'),
    path('add/', views.add_team, name='add'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete')
]
