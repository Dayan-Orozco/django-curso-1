from django import forms
from principal.models import Persona

class PersonaForm(forms.ModelForm):

    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control"}))
    apellidos = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={"class":"form-control"}))
    correo = forms.EmailField(label="Correo electronico", widget=forms.EmailInput(attrs={"class":"form-control"}))

    class Meta:
        model = Persona
        fields = "__all__"

# verbose_name = 'ModelName'
# verbose_name_plural = 'ModelNames'