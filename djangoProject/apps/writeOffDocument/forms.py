from django import forms
from .models import WriteOffDocument


class WriteOffDocumentModelForm(forms.ModelForm):
    class Meta:
        model = WriteOffDocument
        fields = [
            'date',
            'quantity',
            'goods_id',
            'manager_id'
        ]