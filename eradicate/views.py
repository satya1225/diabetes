# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic

from .models import PatientHist
from .forms import PatientHistForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PatientHistForm(request.POST)
        if form.is_valid():
            form.save()
            """patient = PatientHistForm()
            patient.first_name = form.cleaned_data['first_name']
            patient.middle_name = form.cleaned_data['middle_name']
            patient.last_name = form.cleaned_data['last_name']
            patient.sex = form.cleaned_data['sex']
            patient.date_of_birth = form.cleaned_data['date_of_birth']
            patient.height = form.cleaned_data['height']
            patient.weight = form.cleaned_data['weight']
            patient.email_id = form.cleaned_data['email_id']
            patient.phone_no = form.cleaned_data['phone_no']

            patient.diabetes = form.cleaned_data['diabetes']
            patient.diabetes_long = form.cleaned_data['diabetes_long']
            patient.hypertension = form.cleaned_data['hypertension']
            patient.hypertension_long = form.cleaned_data['hypertension_long']
            patient.obesity = form.cleaned_data['obesity']
            patient.obesity_long = form.cleaned_data['obesity_long']
            patient.pcod = form.cleaned_data['pcod']
            patient.pcod_long = form.cleaned_data['pcod_long']
            patient.thyroid = form.cleaned_data['thyroid']
            patient.thyroid_long = form.cleaned_data['thyroid_long']
            patient.heartdiease = form.cleaned_data['heartdiease']
            patient.heartdiease_long = form.cleaned_data['heartdiease_long']
            patient.liverdisease = form.cleaned_data['liverdisease']
            patient.liverdisease_long = form.cleaned_data['liverdisease_long']
            patient.kidney = form.cleaned_data['kidney']
            patient.kidney_long = form.cleaned_data['kidney_long']
            patient.familyhistory = form.cleaned_data['familyhistory']
            patient.currentmed = form.cleaned_data['currentmed']
            patient.foodhabit = form.cleaned_data['foodhabit']
            patient.hba1c = form.cleaned_data['hba1c']
            patient.fasting = form.cleaned_data['fasting']
            patient.pp = form.cleaned_data['pp']

            #patient.save()
            #return HttpResponse("dob is" + str(patient.date_of_birth))
            """
            return HttpResponseRedirect(reverse('eradicate:menu') )
    else:
        form = PatientHistForm()
    return render(request, 'eradicate/index.html', {'form': form})

def menu(request):
    return HttpResponse("Your data is saved")
 #   question = get_object_or_404(Question, pk=question_id)
  #  return render(request, 'polls/detail.html', {'question': question})
