from django.urls import path

from userint import views

urlpatterns = [
    path('workers/<str:param>', views.index),
    path('query/<str:task_id>/', views.query_task),
]
