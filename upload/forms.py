# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class DocForm(forms.Form):
    docfile1 = forms.FileField(
        label='Select',
        help_text='max. 42 megabytes'
    )
