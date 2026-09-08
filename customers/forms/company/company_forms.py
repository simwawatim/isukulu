from customers.models import Client
from django import forms

class CompanyRegistrationForm(forms.Form):
    company_name = forms.CharField(max_length=100, label="Company / School Name")
    admin_first_name = forms.CharField(max_length=30, label="Your First Name")
    admin_last_name = forms.CharField(max_length=30, label="Your Last Name")
    admin_email = forms.EmailField(label="Your Email")
    admin_password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean_subdomain(self):
        subdomain = self.cleaned_data["subdomain"].lower()
        if subdomain in ("public", "www", "admin"):
            raise forms.ValidationError("This subdomain is reserved.")
        if Client.objects.filter(schema_name=subdomain).exists():
            raise forms.ValidationError("This subdomain is already taken.")
        return subdomain