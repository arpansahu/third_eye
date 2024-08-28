from django.db import models


# Create your models here.
class Symptoms(models.Model):
    symptom_name = models.CharField(max_length=100)


class SymptomsAndPatientName(models.Model):
    patient_name = models.CharField(max_length=50)
    symptom_one = models.CharField(max_length=50)
    symptom_two = models.CharField(max_length=50)
    symptom_three = models.CharField(max_length=50)
    symptom_four = models.CharField(max_length=50)
    symptom_five = models.CharField(max_length=50)


class Hospitals(models.Model):
    name = models.CharField(max_length=300, null=False)
    address = models.CharField(max_length=300, null=False)
    street = models.CharField(max_length=300, null=False)
    landmark = models.CharField(max_length=300, null=False)
    locality = models.CharField(max_length=300)
    pincode = models.CharField(max_length=300)
    landline_no = models.CharField(max_length=300)
    latitude = models.FloatField()  # Changed from CharField to FloatField
    longitude = models.FloatField()  # Changed from CharField to FloatField
    altitude = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    district = models.CharField(max_length=100, null=False)
    taluka = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
