from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PaqueteForm
from .models import Paquete


class PaqueteListView(ListView):
    model = Paquete
    template_name = "paquetes/paquete_list.html"
    context_object_name = "paquetes"

    def get_queryset(self):
        # Optimización ORM: un solo JOIN, evita el problema N+1
        return Paquete.objects.select_related("categoria")


class PaqueteDetailView(DetailView):
    model = Paquete
    template_name = "paquetes/paquete_detail.html"
    context_object_name = "paquete"  # <int:pk> en la URL; 404 automático si no existe


# Regla MRO: los mixins SIEMPRE a la izquierda de la vista genérica
class PaqueteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Paquete
    form_class = PaqueteForm
    template_name = "paquetes/paquete_form.html"
    success_url = reverse_lazy("paquete_list")
    success_message = "El paquete «%(nombre)s» fue creado correctamente."


class PaqueteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Paquete
    form_class = PaqueteForm
    template_name = "paquetes/paquete_form.html"
    success_url = reverse_lazy("paquete_list")
    success_message = "El paquete «%(nombre)s» fue actualizado correctamente."


class PaqueteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Paquete
    template_name = "paquetes/paquete_confirm_delete.html"
    success_url = reverse_lazy("paquete_list")
    success_message = "El paquete fue eliminado correctamente."
