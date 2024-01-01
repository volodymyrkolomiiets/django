from django import forms
from django.forms.widgets import NumberInput

FAVORITE_DISH = [
    ("italian", "Italian"),
    ("greek", "Greek"),
    ("turkish", "Turkish")
]

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={"row": 5}))
    email = forms.EmailField(label="Enter email address")
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type':"date"}))
    favorite_dish = forms.ChoiceField(choices=FAVORITE_DISH)
    favorite_dish_radioselect=forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_DISH)
