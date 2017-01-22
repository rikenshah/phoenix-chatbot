from django import forms

class InputForm(forms.Form):
    inputText = forms.CharField(label='Input Text', max_length=2000,widget=forms.Textarea)