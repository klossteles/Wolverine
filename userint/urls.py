from django.urls import path

from userint import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('cgne/', views.cgne, name='cgne'),
    path('image/<str:signal_output_id>', views.image, name='image'),
    path('download-images', views.download_images, name='download_images'),
]
