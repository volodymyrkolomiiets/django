from django import forms


class ApplicationForm(forms.Form):
    name = forms.CharField(label="Name of Applicant", max_length=50)
    address = forms.CharField(label='Address', max_length=100)
    posts = (("Manager", "Manager"), ("Cashier", "Cashier"), ("Operator", "Operator"))
    field = forms.ChoiceField(choices=posts)
    
    
SHIFTS = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening")
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField(help_text="Enter the exact time")
    