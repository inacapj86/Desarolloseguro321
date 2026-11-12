from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .forms import ProductoForm
from .models import Producto


class SoloSusRegistrosMixin(LoginRequiredMixin):
    """Autorizacion en el servidor, a nivel de registro.

    - Usuario normal: solo ve, edita y elimina los productos que creo.
    - Personal (is_staff): ve y administra todos los productos.
    Un producto ajeno responde 404 (no 403) para no revelar que existe.
    """

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(propietario=self.request.user)


class FormularioConUsuarioMixin:
    form_class = ProductoForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ProductoListView(SoloSusRegistrosMixin, ListView):
    model = Producto
    template_name = 'productos/producto_list.html'
    context_object_name = 'productos'


class ProductoDetailView(SoloSusRegistrosMixin, DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'


class ProductoCreateView(LoginRequiredMixin, FormularioConUsuarioMixin, CreateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto-list')

    def form_valid(self, form):
        # El propietario lo fija el servidor con la sesion autenticada.
        form.instance.propietario = self.request.user
        return super().form_valid(form)


class ProductoUpdateView(SoloSusRegistrosMixin, FormularioConUsuarioMixin, UpdateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto-list')


class ProductoDeleteView(SoloSusRegistrosMixin, DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')
