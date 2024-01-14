from .models import Person
from django import forms

class PersonForm(forms.ModelForm):
    start_year = forms.IntegerField(required=False, label='Start Year')
    end_year = forms.IntegerField(required=False, label='End Year')
    accurate_search = forms.BooleanField(required=False, initial=False, label='Accurate Search')

    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            'BirthDate': forms.TextInput(attrs={'type': 'date'}),  # Assuming BirthDate is a DateField
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False