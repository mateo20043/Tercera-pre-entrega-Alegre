from django import forms
from .models import Usuario, Producto

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)
