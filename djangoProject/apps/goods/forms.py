from django import forms
from .models import Goods


class GoodsModelFormForChange(forms.ModelForm):

    class Meta:
        model = Goods
        fields = [
            'name',
            'category',
        ]

    def clean_name(self):
        data = self.cleaned_data.get('name')
        return data


class GoodsModelForm(forms.ModelForm):

    class Meta:
        model = Goods
        fields = [
            'name',
            'category',
            'count',
            'prise'
        ]