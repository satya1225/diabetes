# -*- coding: utf-8 -*-
from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
class Patient(models.Model):

    MALE_FEMALE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, default='F',choices=MALE_FEMALE, verbose_name="Gender")
    date_of_birth = models.DateField()
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    email_id = models.EmailField(max_length=50, primary_key=True)
    phone_no = models.BigIntegerField()

    def __str__(self):
        return self.first_name

FOOD_HABITS_CHOICES = (
    ('V', 'Veg'),
     ('N', 'Non-Veg'),
)

class PatientHist(Patient):
    Yes_No = (
        (True, 'Yes'),
        (False, 'No'),
    )

    diabetes = models.BooleanField(default=False, choices=Yes_No, verbose_name="Have you ever been diagnosed with Diabetes?")
    diabetes_long = models.CharField(max_length=20, blank=True)
    hypertension = models.BooleanField(default=False,choices=Yes_No, verbose_name="Have you ever been diagnosed with Hypertension?")
    hypertension_long = models.CharField(max_length=20, blank=True)
    obesity = models.BooleanField(default=False,choices=Yes_No, verbose_name="Are you obese?")
    obesity_long = models.CharField(max_length=20, blank=True)
    pcod = models.BooleanField(default=False,choices=Yes_No, verbose_name="Have you ever been diagnosed with PCOD/PCOS (Females Only)?")
    pcod_long= models.CharField(max_length=20, blank=True)
    thyroid = models.BooleanField(default=False,choices=Yes_No, verbose_name="Have you ever been diagnosed with Thyroid problems?")
    thyroid_long = models.CharField(max_length=20, blank=True)
    heartdiease = models.BooleanField(default=False,choices=Yes_No, verbose_name="Have you ever been diagnosed with Heart desease?")
    heartdiease_long = models.CharField(max_length=20, blank=True)
    liverdisease = models.BooleanField(default=False,choices=Yes_No, verbose_name="Have you ever been diagnosed with Liver desease?")
    liverdisease_long = models.CharField(max_length=20, blank=True)
    kidney = models.BooleanField(default=False,choices=Yes_No, verbose_name="Have you ever been diagnosed with Kidney desease?")
    kidney_long = models.CharField(max_length=20, blank=True)
    familyhistory = models.BooleanField(default=False,choices=Yes_No, verbose_name="Do you have a history of Diabetes in your family?")
    currentmed = models.CharField(max_length=70, blank=True, verbose_name="Current Medications: ")
    foodhabit= models.CharField(max_length=1, default='V', choices=FOOD_HABITS_CHOICES, verbose_name="What are your food habits?")
    hba1c = models.FloatField(max_length=20, verbose_name="HBA1C results: ")
    fasting = models.FloatField(max_length=20, verbose_name="Your fasting blood sugar results: ")
    pp = models.FloatField(max_length=20, verbose_name="Your PP results: ")

    def __str__(self):
        return self.first_name

class AbstractMenu(models.Model):
    veg_nonveg = models.CharField(max_length=1, default='V', choices=FOOD_HABITS_CHOICES)
    item_name = models.CharField(max_length=50)

    class Meta:
        abstract = True

class BreakFastMenu(AbstractMenu):

    def getBreakFastList(self, veg_nveg):
        itemsList = BreakFastMenu.objects.filter(veg_nonveg=veg_nveg).values_list('item_name', flat=True)
        return itemsList

class LunchMenu(AbstractMenu):

    def getLunchList(self, veg_nveg):
        itemsList = LunchMenu.objects.filter(veg_nonveg=veg_nveg).values_list('item_name', flat=True)
        return itemsList

class SnacksMenu(AbstractMenu):

    def getSnacksList(self, veg_nveg):
        itemsList = SnacksMenu.objects.filter(veg_nonveg=veg_nveg).values_list('item_name', flat=True)
        return itemsList

class DinnerMenu(AbstractMenu):

    def getDinnerList(self, veg_nveg):
        itemsList = DinnerMenu.objects.filter(veg_nonveg=veg_nveg).values_list('item_name', flat=True)
        return itemsList
