from django.urls import path

from userint import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('workers/<str:param>', views.index),
    path('query/<str:task_id>/', views.query_task),
    path('cgne/', views.cgne),
    path('cgne/image/<str:task_id>', views.obtain_image),
]
