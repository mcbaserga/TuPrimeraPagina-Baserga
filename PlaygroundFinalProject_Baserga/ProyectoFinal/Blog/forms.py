from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel

# PROFILE
class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["username", "email", "password1", "password2" ]
        help_texts = {k: "" for k in fields}
        
class MyProfileForm(forms.Form):
    imagen = forms.CharField()
    nombre = forms.CharField()
    descripcion = forms.CharField()
    link = forms.CharField()
    email = forms.EmailField()


class UserEditionFormulario(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido", widget=forms.PasswordInput)
    password = None

    class Meta:
        model = UserModel
        fields = ["email", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}



# BLOG
class Blog(forms.Form):
    imagen = forms.CharField(max_length=50, label="Imagen")
    titulo = forms.CharField(label="Titulo", max_length=24)
    subtitulo = forms.CharField(max_length=50, label="Subtítulo")
    cuerpo = forms.CharField(max_length=300, label="Texto")
    autor = forms.CharField(max_length=50, label="Autor")
    fecha = forms.DateTimeField()