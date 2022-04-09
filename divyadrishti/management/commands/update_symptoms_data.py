from django.core.management import BaseCommand
import pandas as pd

from django.conf import settings
from divyadrishti.models import Symptoms
from divyadrishti.machine_learning.machinlearning import listofsymptoms


def startup():
    print("---------------------Update Symptoms Command Started----------------------")

    for symptom in listofsymptoms:
        if not Symptoms.objects.filter(symptom_name=symptom
                                       ).count():
            print(f"added : {symptom}")
            Symptoms.objects.create(symptom_name=symptom
                                    )
        else:
            print(f"already present : {symptom}")
    print("---------------------Update Symptoms Command Ended----------------------")


class Command(BaseCommand):
    def handle(self, *args, **options):
        startup()
