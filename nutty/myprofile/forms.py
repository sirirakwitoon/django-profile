from django import forms


class SubscriberForm(forms.Form):
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'class': 'myemailfield', 'placeholder': "Email address", 'id': 'myInput'}))
