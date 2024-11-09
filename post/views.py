from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Personas
from django.views.generic import CreateView,DetailView, DeleteView,UpdateView
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
    template_name = "post.html"
    model = Post

class usuariosVie(ListView):
    template_name=  "usuarios.html"
    model=Personas
   
class CreatePageView(CreateView):
    model=Post
    template_name="create.html"
    fields=["titulo","descripcion","imagen","precio"]
    success_url=reverse_lazy("post")


class detailPageView(DetailView):
    model=Post
    template_name="detail.html"
    
class updatePageView(UpdateView):
        template_name="update.html"
        model=Post
        fields=["titulo","descripcion", "imagen","precio"]
        success_url=reverse_lazy("post")

class DeletePageView(DeleteView):
    

    template_name="delete.html"
    model=Post 
    success_url=reverse_lazy("post")


