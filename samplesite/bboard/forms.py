from django.forms import ModelForm

from .models import Вb


class BbForm(ModelForm):
    class Meta:
        model = Вb
        fields = ('title', 'content', 'price', 'rubric')
