from django import forms
from .models import *


class Patient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientHistForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    pcod_long = forms.CharField(label="If Yes, how long have you been diagnosed with PCOD/PCOS (Females Only)?",required=False,widget=forms.TextInput(attrs={'class': 'sex pcod'}))
    diabetes_long = forms.CharField(label="If Yes, how long have you been diagnosed with diabetes?",required=False,widget=forms.TextInput(attrs={'class': 'diabetes'}))
    hypertension_long = forms.CharField(label="If Yes, how long have you been diagnosed with hypertension?",required=False,widget=forms.TextInput(attrs={'class': 'hypertension'}))
    obesity_long = forms.CharField(label="If Yes, how long have you been obese?",required=False,widget=forms.TextInput(attrs={'class': 'obesity'}))
    thyroid_long = forms.CharField(label="If Yes, how long have you been diagnosed with thyroid?",required=False,widget=forms.TextInput(attrs={'class': 'thyroid'}))
    heartdiease_long = forms.CharField(label="If Yes, how long have you been diagnosed with heart desease?",required=False,widget=forms.TextInput(attrs={'class': 'heartdiease'}))
    liverdisease_long = forms.CharField(label="If Yes, how long have you been diagnosed with liver disease?",required=False,widget=forms.TextInput(attrs={'class': 'liverdisease'}))
    kidney_long = forms.CharField(label="If Yes, how long have you been diagnosed with kidney desease?",required=False,widget=forms.TextInput(attrs={'class': 'kidney'}))

    class Meta:
        model = PatientHist
        fields = '__all__'

        widgets = {
            'sex': forms.RadioSelect(attrs={'onclick': "makeRequired(id,name);"}),
            'date_of_birth': forms.SelectDateWidget(years=range(2020, 1939, -1)),
            # 'date_of_birth': forms.DateInput(),
            'diabetes': forms.RadioSelect(attrs={'onclick': "makeRequired(id,name);"}),
            'hypertension': forms.RadioSelect(attrs={'onclick': "makeRequired(id,name);"}),
            'obesity': forms.RadioSelect(attrs={'onclick': "makeRequired(id,name);"}),
            'pcod': forms.RadioSelect(attrs={'class': 'sex', 'onclick': "makeRequired(id,name);"}),
            # 'pcod_long': forms.CharField(attrs={'class': 'sex'}),
            'thyroid': forms.RadioSelect(attrs={'onclick': "makeRequired(id,name);"}),
            'heartdiease': forms.RadioSelect(attrs={'onclick': "makeRequired(id,name);"}),
            'liverdisease': forms.RadioSelect(attrs={'onclick': "makeRequired(id,name);"}),
            'kidney': forms.RadioSelect(attrs={'onclick': "makeRequired(id,name);"}),
            'familyhistory': forms.RadioSelect,
            'foodhabit': forms.RadioSelect,
        }
