from django.urls import path
from quickstart import views

urlpatterns = [
    path('list/', views.StudentListView.as_view()),
    path('create/', views.StudentCreateView.as_view()),
    path('retrieve/<int:pk>', views.StudentRetrieveView.as_view()),
    path('update/<int:pk>', views.StudentUpdateView.as_view()),
    path('destroy/<pk>', views.StudentDestroyView.as_view()),
]
