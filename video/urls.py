from django.urls import path
from . import views

urlpatterns = [
    path('uploads/', views.upload_video),
    path('',views.videos),
    path('date/',views.videos_sort_by_date)
]