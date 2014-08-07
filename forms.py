from django.forms import ModelForm, Form, CharField
from .models import Page

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']


class PageSearchForm(Form):
    terms = CharField(label='Search')
