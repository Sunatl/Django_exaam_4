from django.urls import path
from .views import *

urlpatterns = [
    path("",base,name="base"),
    
    # Movie
    path("Movie",ListView.as_view(),name="list_m"),
    path("create",CreateView.as_view(),name="create_m"),
    path("update/<int:pk>",UpdateView.as_view(),name="update_m"),
    path("detail/<int:pk>",DetailView.as_view(),name="detail_m"),
    path("delete/<int:pk>",DeleteView.as_view(),name="delete_m")
]
