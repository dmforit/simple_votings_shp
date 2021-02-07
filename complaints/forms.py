from django import forms


class ComplaintForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    title = forms.CharField()
