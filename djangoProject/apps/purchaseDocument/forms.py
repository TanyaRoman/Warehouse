from django import forms
from .models import PurchaseDocument


class PurchaseDocumentModelForm(forms.ModelForm):
    class Meta:
        model = PurchaseDocument
        fields = [
            'date',
            'quantity',
            'goods_id',
            'manager_id'
        ]