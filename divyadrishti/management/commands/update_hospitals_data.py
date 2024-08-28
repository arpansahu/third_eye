from django.core.management import BaseCommand
import pandas as pd

from django.conf import settings
from divyadrishti.models import Hospitals


def startup():
    print("---------------------Update Hospitals Command Started----------------------")

    df = pd.read_csv(str(settings.BASE_DIR) + '/nin-health-facilities.csv', encoding="ISO-8859-1")
    df = df.iloc[:, 1:]
    for index, row in df.iterrows():
        try:
            if not Hospitals.objects.filter(name=row.values[0], address=row.values[1],
                                            street=row.values[2], landmark=row.values[3],
                                            locality=row.values[3],
                                            pincode=row.values[5], landline_no=row.values[6],
                                            latitude=row.values[7],
                                            longitude=row.values[8],
                                            altitude=row.values[9], type=row.values[10], state=row.values[11],
                                            district=row.values[12],
                                            taluka=row.values[13], block=row.values[14]
                                            ).count():
                print(f"added : {row}")
                Hospitals.objects.create(name=row.values[0], address=row.values[1],
                                            street=row.values[2], landmark=row.values[3],
                                            locality=row.values[3],
                                            pincode=row.values[5], landline_no=row.values[6],
                                            latitude=row.values[7],
                                            longitude=row.values[8],
                                            altitude=row.values[9], type=row.values[10], state=row.values[11],
                                            district=row.values[12],
                                            taluka=row.values[13], block=row.values[14]
                                        )
        except Exception as e:
            pass
        else:
            print(f"already present : {row}")
    print("---------------------Update Locations Command Ended----------------------")


class Command(BaseCommand):
    def handle(self, *args, **options):
        startup()
