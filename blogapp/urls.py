from django.urls import path
#from . import views
from .views import IndexView, DetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('',IndexView.as_view(), name="index"),
    path('detail/<int:pk>', DetailView.as_view(), name = "detail"),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('detail/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('detail/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    ]