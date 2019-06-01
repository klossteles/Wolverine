from django.urls import path

from userint import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('cgne/', views.cgne, name='cgne'),
    path('cgne/image/<str:task_id>', views.obtain_image),
    path('image/<str:task_id>', views.image, name='image'),
]
