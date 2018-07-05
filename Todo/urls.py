from django.urls import path
from . import views

app_name = 'Todo'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:pk>/delete/', views.delete,name = 'delete'),
	path('<int:pk>/completed/', views.completed,name = 'completed'),
]