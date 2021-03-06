#coding=utf-8
from django import forms
from django.core.exceptions import ValidationError

from .models import Item

# class ItemForm(forms.Form):
#     item_text = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter a to-do item',
#             'class': 'form-control input-lg',
#         }),
#     )

EMPTY_LIST_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You're already got this in your list"

class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text', )
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
                'required': False,
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }
    
class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)
