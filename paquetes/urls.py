from django.urls import path

from . import views

urlpatterns = [
    path("", views.PaqueteListView.as_view(), name="paquete_list"),
    path("paquete/<int:pk>/", views.PaqueteDetailView.as_view(), name="paquete_detail"),
    path("nuevo/", views.PaqueteCreateView.as_view(), name="paquete_create"),
    path("paquete/<int:pk>/editar/", views.PaqueteUpdateView.as_view(), name="paquete_update"),
    path("paquete/<int:pk>/eliminar/", views.PaqueteDeleteView.as_view(), name="paquete_delete"),
]
