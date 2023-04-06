from django.urls import path
from .views import CategoryListCreateApiView, TagListCreateApiView, CategoryRUDApiView, TagRUDApiView, BlogListCreateApiView, BlogRUDApiView
urlpatterns = [
    path('category-list-create/', CategoryListCreateApiView.as_view()),
    path('tag-list-create/', TagListCreateApiView.as_view()),
    path('blog-list-create/', BlogListCreateApiView.as_view()),
    path('tag-rud/<int:pk>/', TagRUDApiView.as_view()),
    path('category-rud/<int:pk>/', CategoryRUDApiView.as_view()),
    path('article-rud/<int:pk>/', BlogRUDApiView.as_view()),
]
