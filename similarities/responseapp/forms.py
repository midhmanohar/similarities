from django import forms

class MyForm(forms.Form):
 name = forms.CharField(label='Enter your string', max_length=100)
 resl = forms.IntegerField(label='value', max_length=100)
