from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type':'text',
            'placeholder':'Enter Username',
            'id':'username',
            'name':'username',
            'required': '',
        })
    class Meta:
        model = User
        fields = ['username', 'password']

class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=101)
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    # email = forms.EmailField(required=True)

    # class Meta:
    #     model= User
    #     fields = ['username', 'email', 'password', 'password']
    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user