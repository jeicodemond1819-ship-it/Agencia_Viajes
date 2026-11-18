from django import forms

from .models import Paquete


class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ["nombre", "destino", "categoria", "descripcion", "precio", "fecha_salida", "cupos", "disponible"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "destino": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "fecha_salida": forms.DateInput(attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"),
            "cupos": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
