from django.urls import path
from .views import AboutListAPIView, TechnologyListAPIView, TechnologyDetailAPIView, TechnologyCreateAPIView, TechnologyUpdateAPIView, TechnologyDestroyAPIView, TechnologyDetailUpdateAPIView, TechnologyListCreateAPIView, TechnologyRetrieveUpdateAPIView

urlpatterns = [
    path('users/', AboutListAPIView.as_view()),
    path('technologies/', TechnologyListAPIView.as_view()),
    path('technologies/create/', TechnologyCreateAPIView.as_view()),
    path('technologies/<int:pk>/', TechnologyDetailAPIView.as_view()),
    path('technologies/<int:pk>/update/', TechnologyUpdateAPIView.as_view()),
    path('technologies/<int:pk>/delete/', TechnologyDestroyAPIView.as_view()),
    path('technologies/<int:pk>/retrieve/update/', TechnologyDetailUpdateAPIView.as_view()),
    path('technologies/<int:pk>/retrieve/delete/', TechnologyDetailUpdateAPIView.as_view()),
    path('technologies/list/create/', TechnologyListCreateAPIView.as_view()),
    path('technologies/<int:pk>/update/', TechnologyRetrieveUpdateAPIView.as_view()),
]