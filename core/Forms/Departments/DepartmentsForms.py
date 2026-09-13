from core.models import Department, Subject, Teacher
from django import forms



class DepartmentForm(forms.ModelForm):
    subjects_input = forms.CharField(
        required=False,
        label="Subjects Offered",
        widget=forms.TextInput(attrs={"placeholder": "Comma-separated, e.g. Mathematics, Physics"}),
    )

    class Meta:
        model = Department
        fields = ["name", "head_of_department"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["head_of_department"].queryset = Teacher.objects.filter(is_active=True)
        self.fields["head_of_department"].required = False
        self.fields["head_of_department"].empty_label = "Vacant"

        if self.instance.pk:
            self.fields["subjects_input"].initial = ", ".join(
                self.instance.subjects.values_list("name", flat=True)
            )

    def save(self, commit=True):
        department = super().save(commit=commit)

        names = [n.strip() for n in self.cleaned_data.get("subjects_input", "").split(",") if n.strip()]
        subjects = [Subject.objects.get_or_create(name=name)[0] for name in names]
        department.subjects.set(subjects)

        return department