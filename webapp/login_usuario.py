from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'w-full p-2 rounded-md shadow-inner border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'w-full p-2 rounded-md shadow-inner border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'}))
