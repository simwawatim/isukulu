from django import forms
from customers.models import Tier


class TierForm(forms.ModelForm):
    class Meta:
        model = Tier
        fields = ["name", "price", "student_limit", "description", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full rounded-lg border-gray-200 text-sm"}),
            "price": forms.NumberInput(attrs={"class": "w-full rounded-lg border-gray-200 text-sm"}),
            "student_limit": forms.NumberInput(attrs={"class": "w-full rounded-lg border-gray-200 text-sm"}),
            "description": forms.Textarea(attrs={"rows": 2, "class": "w-full rounded-lg border-gray-200 text-sm"}),
        }