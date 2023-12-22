from django import forms
from .models import Order, Comment


class GoodsOrderingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address', 'phone_number')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


