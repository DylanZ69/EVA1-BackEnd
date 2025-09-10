from django import forms
from .models import Mascota, Refugio, Usuario, Solicitud, Seguimiento

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'

class RefugioForm(forms.ModelForm):
    class Meta:
        model = Refugio
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'

class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = '__all__'
