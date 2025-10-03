# predictor/forms.py

from django import forms


class IrisForm(forms.Form):
    sepal_length = forms.FloatField(min_value=0, label='Sepal Length (cm)')
    sepal_width = forms.FloatField(min_value=0, label='Sepal Width (cm)')
    petal_length = forms.FloatField(min_value=0, label='Petal Length (cm)')
    petal_width = forms.FloatField(min_value=0, label='Petal Width (cm)')