from django.urls import path
from .views import HomePageView, usuariosVie, CreatePageView, detailPageView, updatePageView, DeletePageView


urlpatterns = [
    path("", HomePageView.as_view(), name = "post"),
    path("usuarios", usuariosVie.as_view(), name = "usuario"),
    path("post/create",CreatePageView.as_view(),name="create"),
    path("post/detail/<int:pk>",detailPageView.as_view(),name="detail"),
    path("post/detail/<int:pk>/update",updatePageView.as_view(),name="update"),
    path("post/detail/<int:pk>/delete",DeletePageView.as_view(),name="delete"),


]