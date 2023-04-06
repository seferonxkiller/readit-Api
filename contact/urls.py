from django.urls import path
from .views import ContactListCreateApiView


urlpatterns = [
    path('list-create', ContactListCreateApiView.as_view())
]
