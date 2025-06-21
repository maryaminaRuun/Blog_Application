
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name =  forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))



    class meta:
        model = User
        fields =('username', 'first_name', 'last_name', 'email',  'password1', 'password2' )


    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['username'].help_text ='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only</small></snap>'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password1'].help_text =' <ul class="form-text text-muted"><small> <li>.Your password can not be a commonly used password.</li>  <li>.Your password can not be entirely numeric.</li></small></ul>'
        self.fields['password2'].widget.attrs['class']= 'form-control'
        self.fields['password2'].lebel=''
        self.fields['password2'].help_text =' <ul class="form-text text-muted"> <small> <li>.Enter the same password as before, for verification. </li></small></ul>'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name =  forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username =  forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login =  forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_supperuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_stuff=  forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active =  forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined =  forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))



    class meta:
        model = User
        fields =('username', 'first_name', 'last_name', 'email',  'password', 'last_login','is_supperuser', 'is_stuff', 'is_active', 'date_joined' )


