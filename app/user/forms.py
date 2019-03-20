from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Your name', 'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Email', 'class':'form-control'}))
    password = forms.CharField(label='Password', min_length=4, widget=forms.PasswordInput(attrs={'autocomplete':'off','placeholder':'Password', 'class':'form-control'}))


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Email', 'class': 'form-control' }))
    password = forms.CharField(label='Password', min_length=4, widget=forms.PasswordInput(attrs={'autocomplete':'off','placeholder':'Password', 'class':'form-control'}))
