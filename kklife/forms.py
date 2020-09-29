from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label= "Name" )
    email = forms.EmailField(label='Email')
    ph_no = forms.NumberInput(label='Phone No.')
    addrs = forms.TextInput(label='Address')
    city = forms.CharField(label = 'City')
    zip_code = forms.NumberInput(label='Zip')

