from django import forms

from polls.models import Person


class AddPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
