from django import forms

class TodoForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'My awesome list', 'aria-describedby':'add-btn'}))

class CreateNewList(forms.Form):
	name = forms.CharField(label="Name", max_length=80)
	check = forms.BooleanField(required=False)