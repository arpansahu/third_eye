# importing render from django - shortcuts
import requests
from django.shortcuts import render
from .models import Symptoms, SymptomsAndPatientName, Hospitals
from django.conf import settings
# importing pickle to predict with the help of pickled model in naivebayesbernouli.pkl
import pickle
# list of symptoms and list of diseases
import geoip2.database
from .machine_learning.machinlearning import disease, listofsymptoms
from django.http import JsonResponse
import json
from math import radians, degrees, cos, sin, asin, sqrt
from django.db.models import Q

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

    print(symp_objs)
    return render(request, 'divyadrishti.html', {"Symptoms": symp_objs})



def get_bounds(lat, lon, radius_km):
    # Radius of Earth in km
    R = 6371

    # Convert latitude and longitude from degrees to radians
    lat_rad = radians(lat)
    lon_rad = radians(lon)

    # Calculate the bounds
    dlat = radius_km / R
    dlon = radius_km / (R * cos(lat_rad))

    min_lat = lat - (dlat * (180 / 3.14159))
    max_lat = lat + (dlat * (180 / 3.14159))
    min_lon = lon - (dlon * (180 / 3.14159))
    max_lon = lon + (dlon * (180 / 3.14159))

    return min_lat, max_lat, min_lon, max_lon

def distance(lat1, lon1, lat2, lon2):
    # Calculate the distance between two points on Earth
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of Earth in km

    return c * r

def get_hospitals_within_radius(lat, lon, radius_km):
    min_lat, max_lat, min_lon, max_lon = get_bounds(lat, lon, radius_km)
    
    # Filter hospitals within bounding box
    hospitals = Hospitals.objects.filter(
        latitude__gte=min_lat, latitude__lte=max_lat,
        longitude__gte=min_lon, longitude__lte=max_lon
    )

    return hospitals

def table(request):
    print("=============================================================")
    print("Inside Table View")
    lat = request.GET.get('latitude')
    lon = request.GET.get('longitude')

    print("================================================================")
    print('latitude is:', lat, 'longitude is:', lon)

    # Ensure lat and lon are floats
    lat = float(lat) if lat else None
    lon = float(lon) if lon else None

    if lat and lon:
        finallist = get_hospitals_within_radius(lat, lon, radius_km=25)
    else:
        finallist = []

    return render(request, 'table.html', {"hospitalList": finallist})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    x_real_ip = request.META.get('HTTP_X_REAL_IP')
    
    # Use X-Real-IP if available, otherwise fall back to X-Forwarded-For
    if x_real_ip:
        ip = x_real_ip
    elif x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Optionally filter out internal IP ranges if needed
    if ip.startswith('10.') or ip.startswith('192.168') or ip.startswith('172.'):
        return None  # Handle as needed

    return ip




def get_location_by_ip(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
        if data.get('bogon'):
            return {
                'ip': ip,
                'error': 'Bogon IP address, cannot determine location',
                'message': 'This IP address is not routable on the public internet.'
            }
        return {
            'ip': ip,
            'city': data.get('city'),
            'region': data.get('region'),
            'country': data.get('country'),
            'location': data.get('loc'),  # Latitude and Longitude
            'organization': data.get('org'),
            'postal': data.get('postal'),
        }
    except requests.RequestException:
        return {'error': 'Unable to reach the geolocation service'}



def user_location_view(request):
    ip = get_client_ip(request)
    if not ip:
        return JsonResponse({
            'error': 'Unable to determine public IP address.'
        })
    
    location = get_location_by_ip(ip)
    return JsonResponse(location)

def debug_headers_view(request):
    headers = {
        'X-Forwarded-For': request.META.get('HTTP_X_FORWARDED_FOR'),
        'X-Real-IP': request.META.get('HTTP_X_REAL_IP'),
        'Remote-Addr': request.META.get('REMOTE_ADDR'),
    }
    return JsonResponse(headers)