from django.urls import path
from quickstart import views

urlpatterns = [
    path('api', views.StudentView.as_view()),
]
