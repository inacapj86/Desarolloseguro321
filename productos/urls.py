from django.urls import path

from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)


urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/nuevo/', ProductoCreateView.as_view(), name='producto-create'),
    path('producto/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto-update'),
    path('producto/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto-delete'),
]