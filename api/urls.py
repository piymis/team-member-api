from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.TeamMemberList.as_view()),
    path('api/<int:pk>/', views.TeamMemberDetail.as_view()),
]