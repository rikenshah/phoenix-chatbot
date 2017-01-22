from django import forms

class TrainingForm(forms.Form):
    inputText = forms.CharField(label='Query', max_length=2000,widget=forms.Textarea)