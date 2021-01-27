# from django import forms
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control",
#                 "id": "user-password"
#             }
#         )
#     )

    # def clean_username(self):
    #     username = self.cleaned_data("username")


from django import forms
from .models import Manager


class ManagerModelFormForChange(forms.ModelForm):

    class Meta:
        model = Manager
        fields = [
            'surname',
            'name',
            'name_second',
        ]

    def clean_name(self):
        data = self.cleaned_data.get('name')
        return data


class ManagerModelForm(forms.ModelForm):

    class Meta:
        model = Manager
        fields = [
            'surname',
            'name',
            'name_second',
            'date_of_birth',
            'address',
            'data_of_hiring'
        ]

