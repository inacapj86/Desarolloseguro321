# productos/forms.py
from decimal import Decimal
from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'costo_interno']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Minimizacion: el costo interno solo se muestra y se acepta si el
        # usuario es personal autorizado. Si el campo no existe en el form,
        # un POST manipulado con "costo_interno" se ignora.
        if user is None or not user.is_staff:
            del self.fields['costo_interno']

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < Decimal('0.01'):
            raise forms.ValidationError('El precio debe ser al menos 0,01.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if not 0 <= stock <= 10000:
            raise forms.ValidationError('El stock debe estar entre 0 y 10000.')
        return stock

    def clean_costo_interno(self):
        costo = self.cleaned_data['costo_interno']
        if costo < 0:
            raise forms.ValidationError('El costo no puede ser negativo.')
        return costo
