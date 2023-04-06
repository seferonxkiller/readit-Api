from django.urls import path
from .views import FeedbackListCreateApiView, FeedbackRUDApiView


urlpatterns = [
    path('list-create/', FeedbackListCreateApiView.as_view()),
    path('rud/<int:pk>/', FeedbackRUDApiView.as_view()),
]
