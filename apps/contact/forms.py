from django import forms


class ContactRegisterForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True, min_length=11, max_length=11)
    area = forms.CharField(required=True)
    description = forms.CharField(required=False)


class ContactLoginForm(forms.Form):
    phone = forms.CharField(required=True, min_length=11, max_length=11)
    password = forms.CharField(required=True, max_length=9)


class ContactCheck(forms.Form):
    pk = forms.IntegerField(required=True)
    checkState = forms.IntegerField(required=True)
    checkDescription = forms.CharField(required=False)
