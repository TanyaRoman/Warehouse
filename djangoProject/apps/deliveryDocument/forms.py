from django import forms
from .models import DeliveryDocument


class DeliveryDocumentModelForm(forms.ModelForm):
    class Meta:
        model = DeliveryDocument
        fields = [
            'quantity',
            'write_off_document_id'
        ]