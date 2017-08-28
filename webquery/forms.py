# -*- coding: utf-8 -*-
from django import forms
from .result import DataSchema

class QueryForm(forms.Form):
    experiment = forms.ChoiceField(label='эксперимент')
    hybrid = forms.ChoiceField(label='гибрид', required=False)

    cnt = 0

    description = DataSchema[cnt][3]
    control_0 = forms.BooleanField(label = description, required = False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_1 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_2 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_3 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_4 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_5 = forms.BooleanField(label = description, required = False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_6 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_7 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_8 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_9 = forms.BooleanField(label = description, required = False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_10 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_11 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_12 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_13 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_14 = forms.BooleanField(label = description, required = False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_15 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_16 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_17 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_18 = forms.BooleanField(label=description, required=False)
    cnt += 1

    description = DataSchema[cnt][3]
    control_19 = forms.BooleanField(label=description, required=False)
    cnt += 1

