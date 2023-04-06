from rest_framework import generics, permissions
from .models import Feedback
from .serializers import FeedbackSerializer
from .permissions import IsAdminUserOrReadOnly


class FeedbackListCreateApiView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAdminUserOrReadOnly]

