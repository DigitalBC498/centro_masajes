from django import forms

class TurnoForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombre'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_telefono'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'id_fecha'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'id': 'id_hora'}))
    tipo_masaje = forms.ChoiceField(
        choices=[
            ('relajante', 'Masaje Relajante'),
            ('descontracturante', 'Masaje Descontracturante'),
            ('facial', 'Masaje Facial')
        ],
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_tipo_masaje'})
    )
