from django import forms
class usersForm(forms.Form):
    uname=forms.CharField(label="Enter User Name",max_length = 20,required=True,widget=forms.TextInput(attrs={'class':'form-control m-3'}))
    passw=forms.CharField(label="Enter password",max_length = 20,required=True,widget=forms.TextInput(attrs={'class':'form-control m-3'}))
