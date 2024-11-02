from django.shortcuts import render
from django.template import loader
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy

def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())



# Movie

class MovieCreate(CreateView):
    model = Movie
    fields = ['name','image','description','vedio','zhanr']
    template_name = "create_m.html"
    success_url = reverse_lazy("list_m")
    
class MovieList(ListView):
    model = Movie
    template_name = 'list_m.html'
    
class MovieDetail(DetailView):
    model = Movie
    template_name = 'detail_m.html'
    
class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name','image','description','vedio','zhanr']
    template_name = "update_m.html"
    success_url = reverse_lazy("list_m")
    
class MovieDelete(DeleteView):
    model = Movie
    template_name = 'delete_m.html'
    success_url = reverse_lazy("list_m")

# Order
class OrderCreate(CreateView):
    model = Order
    fields = ['name','user','amount']
    template_name = "create_o.html"
    success_url = reverse_lazy("list_o")
    
class OrderList(ListView):
    model = Order
    template_name = 'list_o.html'
    
class OrderDetail(DetailView):
    model = Order
    template_name = 'detail_o.html'
    
class OrderUpdate(UpdateView):
    model = Order
    fields = ['name','user','amount']
    template_name = "update_o.html"
    success_url = reverse_lazy("list_o")
    
class OrderDelete(DeleteView):
    model = Order
    template_name = 'delete_o.html'
    success_url = reverse_lazy("list_o")