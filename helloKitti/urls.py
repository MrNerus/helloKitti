from django.urls import path
from . import views as kittyView
from .views import API_getBlogs, API_getBlog, API_getNBlogs

urlpatterns = [
    path('api/blogs/', API_getBlogs.as_view()),
    path('api/blogs/all/', API_getBlogs.as_view()),
    path('api/blog/<int:id>', API_getBlog.as_view()),
    path('api/blogs/<int:numberOfPost>', API_getNBlogs.as_view()),
    path('media/BlogImages/<str:img>', kittyView.get_image),
]