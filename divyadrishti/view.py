# importing render from django - shortcuts

from django.shortcuts import render
from .models import Symptoms, SymptomsAndPatientName, Hospitals
from django.conf import settings
# importing pickle to predict with the help of pickled model in naivebayesbernouli.pkl
import pickle
# list of symptoms and list of diseases

from .machine_learning.machinlearning import disease, listofsymptoms

# our main function for divyadrishti app
def divya_drishti(request):
    # Making an Object if SymptomList for sending the list from database to forms

    symp_objs = Symptoms.objects.all()
    if request.method == "POST":

        # here are some variable lists
        listforinputsymptoms = []
        for x in range(0, len(listofsymptoms)):
            listforinputsymptoms.append(0)

        nameAndsymptomlistfromuse = []

        # Receiving data from the form

        pname = request.POST['pname']
        s1 = Symptoms.objects.get(id=request.POST['Symptom1'])
        s2 = Symptoms.objects.get(id=request.POST['Symptom2'])
        s3 = Symptoms.objects.get(id=request.POST['Symptom3'])
        s4 = Symptoms.objects.get(id=request.POST['Symptom4'])
        s5 = Symptoms.objects.get(id=request.POST['Symptom5'])

        # saving all the data to list nameAndsymptomlistfromuse which we created earlier
        nameAndsymptomlistfromuse.append(pname)
        nameAndsymptomlistfromuse.append(s1.symptom_name)
        nameAndsymptomlistfromuse.append(s2.symptom_name)
        nameAndsymptomlistfromuse.append(s3.symptom_name)
        nameAndsymptomlistfromuse.append(s4.symptom_name)
        nameAndsymptomlistfromuse.append(s5.symptom_name)

        # sending only symptoms data in the symptom_list_from_use

        symptom_list_from_use = nameAndsymptomlistfromuse[1:len(nameAndsymptomlistfromuse)]

        # making an object of symptomandpatienname model in final_data variable to save it further

        final_data = SymptomsAndPatientName(patient_name=pname, symptom_one=s1.symptom_name, symptom_two=s2.symptom_name,
                                            symptom_five=s5.symptom_name, symptom_three=s3.symptom_name,
                                            symptom_four=s4.symptom_name)

        # finally saving all the data to the database
        final_data.save()

        # matching symptoms and making listforinputsymptoms ready for the prediction
        for k in range(0, len(listofsymptoms)):
            for z in symptom_list_from_use:
                if z == listofsymptoms[k]:
                    listforinputsymptoms[k] = 1

        print(listforinputsymptoms)

        # unpickling and predicting the data
        with open(settings.BASE_DIR + '/divyadrishti/machine_learning/naivebayesbernouli.pkl', 'rb') as f:
            tree_algo = pickle.load(f)

        # predicting the data
        y_pred = tree_algo.predict([listforinputsymptoms])

        # final disease is recieved with the help of disease list since our classifier returned the index of the
        # disease which is actually the code of that disease

        final_disease = disease[y_pred[0]]
        print(y_pred)

        return render(request, 'Results.html',
                      {"name": nameAndsymptomlistfromuse[0], "symptom1": nameAndsymptomlistfromuse[1],
                       "symptom2": nameAndsymptomlistfromuse[2], "symptom3": nameAndsymptomlistfromuse[3],
                       "symptom4": nameAndsymptomlistfromuse[4], "symptom5": nameAndsymptomlistfromuse[5],
                       "disease": final_disease})

    return render(request, 'divyadrishti.html', {"Symptoms": symp_objs})


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
                client_ip = '59.92.10.179'

    import geoip2.database
    reader = geoip2.database.Reader(settings.BASE_DIR + '/divyadrishti/GeoLite2-City.mmdb')
    response = reader.city(client_ip)
    city = response.city.name
    country = response.country.name
    state = response.subdivisions.most_specific.name
    print(state, "this is state")
    lat = response.location.latitude
    lon = response.location.longitude
    print(country, city, 'latitude is:', lat, 'longitude is:', lon)
    print("client ip is :", client_ip)

    hospitals = Hospitals.objects.filter(state=state)

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

    for i in hospitals:
        dis = distance(float(lat), float(i.latitude), float(lon), float(i.longitude))
        if dis < 25:
            finallist.append(i)

    return render(request, 'table.html', {"hospitalList": finallist})
