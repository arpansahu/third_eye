# importing render from django - shortcuts
import MySQLdb
from django.shortcuts import render
from .models import SympTomsList, SumptomAndPatientName

# importing pickle to predict with the help of pickled model in naivebayesbernouli.pkl
import pickle

# list of symptoms and list of diseases

listofsymptoms = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
                  'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
                  'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
                  'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
                  'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                  'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
                  'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
                  'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
                  'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
                  'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
                  'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
                  'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
                  'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
                  'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite',
                  'polyuria', 'family_history', 'mucoid_sputum',
                  'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
                  'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
                  'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
                  'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
                  'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
                  'red_sore_around_nose',
                  'yellow_crust_ooze']

disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
           'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
           ' Migraine', 'Cervical spondylosis',
           'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
           'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
           'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
           'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
           'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
           'Impetigo']


# our main function for divyadrishti app
def divyadrishti(request):
    # Making an Object if SymptomList for sending the list from database to forms

    sympObjs = SympTomsList.objects.all()
    if request.method == "POST":

        # here are some variable lists
        listforinputsymptoms = []
        for x in range(0, len(listofsymptoms)):
            listforinputsymptoms.append(0)

        nameAndsymptomlistfromuse = []

        # Receiving data from the form

        pname = request.POST['pname']
        s1 = SympTomsList.objects.get(id=request.POST['Symptom1'])
        s2 = SympTomsList.objects.get(id=request.POST['Symptom2'])
        s3 = SympTomsList.objects.get(id=request.POST['Symptom3'])
        s4 = SympTomsList.objects.get(id=request.POST['Symptom4'])
        s5 = SympTomsList.objects.get(id=request.POST['Symptom5'])

        # saving all the data to list nameAndsymptomlistfromuse which we created earlier
        nameAndsymptomlistfromuse.append(pname)
        nameAndsymptomlistfromuse.append(s1.symptomName)
        nameAndsymptomlistfromuse.append(s2.symptomName)
        nameAndsymptomlistfromuse.append(s3.symptomName)
        nameAndsymptomlistfromuse.append(s4.symptomName)
        nameAndsymptomlistfromuse.append(s5.symptomName)

        # sending only symptoms data in the symptomlistfromuse

        symptomlistfromuse = nameAndsymptomlistfromuse[1:len(nameAndsymptomlistfromuse)]

        # making an object of symptomandpatienname model in finaldata variable to save it further

        finaldata = SumptomAndPatientName(patientName=pname, symptomOne=s1.symptomName, symptomTwo=s2.symptomName,
                                          symptomFive=s5.symptomName, symptomThree=s3.symptomName,
                                          symptomFour=s4.symptomName)

        # finally saving all the data to the database
        finaldata.save()

        # matching symptoms and making listforinputsymptoms ready for the prediction
        for k in range(0, len(listofsymptoms)):
            for z in symptomlistfromuse:
                if z == listofsymptoms[k]:
                    listforinputsymptoms[k] = 1

        print(listforinputsymptoms)

        # unpickling and predicting the data
        with open('C:\\Users\\arpan\\Dropbox\\Technorigger\\divyadrishti\\naivebayesbernouli.pkl', 'rb') as f:
            treealgo = pickle.load(f)

        # predicting the data
        y_pred = treealgo.predict([listforinputsymptoms])

        # final disease is recieved with the help of disease list since our classifier returned the index of the
        # disease which is actually the code of that disease

        final_disease = disease[y_pred[0]]
        print(y_pred)


        return render(request, 'Results.html',
                      {"name": nameAndsymptomlistfromuse[0], "symptom1": nameAndsymptomlistfromuse[1],
                       "symptom2": nameAndsymptomlistfromuse[2], "symptom3": nameAndsymptomlistfromuse[3],
                       "symptom4": nameAndsymptomlistfromuse[4], "symptom5": nameAndsymptomlistfromuse[5],
                       "disease": final_disease})

    return render(request, 'divyadrishti.html', {"Symptoms": sympObjs})


def table(request):
    from ipware import get_client_ip
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        print("Unable to get the client's IP address")
    else:
        print("We got the client's IP address")
        if is_routable:
            print("The client's IP address is publicly routable on the Internet")
        else:
            print("The client's IP address is private")
            if client_ip == '127.0.0.1':
                import socket
                hostname = socket.gethostname()
                client_ip = socket.gethostbyname(hostname)
                print("Your Computer Name is:" + hostname)
                print("Your Computer IP Address is:" + client_ip)

    import geoip2.database
    reader = geoip2.database.Reader('C:\\Users\\arpan\\Dropbox\\Technorigger\\divyadrishti\\GeoLite2-City.mmdb')
    response = reader.city('122.168.45.195')
    city = response.city.name
    country = response.country.name
    lat = response.location.latitude
    lon = response.location.longitude
    print(country, city, 'latitude is:', lat, 'longitude is:', lon)
    print("client ip is :", client_ip)

    # Python 3 program to calculate Distance Between Two Points on Earth
    from math import radians, cos, sin, asin, sqrt

    def distance(lat1, lat2, lon1, lon2):
        # The math module contains a function named
        # radians which converts from degrees to radians.
        lon1 = radians(lon1)
        lon2 = radians(lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371

        # calculate the result
        return (c * r)

    finallist = []

    db = MySQLdb.connect(user='root', db='divyadrishti', passwd='kesarkadam302', host='localhost')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM hopitallist where State_Name like 'Madhya Pradesh'", )
    names = [list(row) for row in cursor.fetchall()]
    db.close()

    try:
        for i in names:
            dis = distance(float(lat), float(i[8]), float(lon), float(i[9]))
            if dis < 25:
                i[0] = dis
                finallist.append(i)

    except:
        pass
    for j in finallist:
        for n, i in enumerate(j):
            if i == 'None':
                j[n] = ''
    from operator import itemgetter
    finallist.sort(key=itemgetter(0))

    return render(request, 'table.html', {"hospitalList": finallist})
