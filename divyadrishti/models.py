from django.db import models


# Create your models here.
class SympTomsList(models.Model):
    symptomName = models.CharField(max_length=100)


class SumptomAndPatientName(models.Model):
    patientName = models.CharField(max_length=50)
    symptomOne = models.CharField(max_length=50)
    symptomTwo = models.CharField(max_length=50)
    symptomThree = models.CharField(max_length=50)
    symptomFour = models.CharField(max_length=50)
    symptomFive = models.CharField(max_length=50)
