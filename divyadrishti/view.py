import requests
import pickle
from math import radians, degrees, cos, sin, asin, sqrt

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Q

from .models import Symptoms, SymptomsAndPatientName, Hospitals
from .machine_learning.machinlearning import disease, listofsymptoms


# Main function for divyadrishti app
def divya_drishti(request):
    symp_objs = Symptoms.objects.all()

    if request.method == "POST":
        # Initialize symptom input list
        listforinputsymptoms = [0] * len(listofsymptoms)

        # Retrieve data from the form
        pname = request.POST['pname']
        symptoms_selected = [
            Symptoms.objects.get(id=request.POST[f'Symptom{i}']).symptom_name
            for i in range(1, 6)
        ]

        # Save patient data to the database
        final_data = SymptomsAndPatientName(
            patient_name=pname,
            symptom_one=symptoms_selected[0],
            symptom_two=symptoms_selected[1],
            symptom_three=symptoms_selected[2],
            symptom_four=symptoms_selected[3],
            symptom_five=symptoms_selected[4]
        )
        final_data.save()

        # Prepare input symptoms list for prediction
        for i, symptom in enumerate(listofsymptoms):
            if symptom in symptoms_selected:
                listforinputsymptoms[i] = 1

        # Predict the disease using the pickled model
        with open(settings.BASE_DIR + '/divyadrishti/machine_learning/naivebayesbernouli.pkl', 'rb') as f:
            tree_algo = pickle.load(f)
        y_pred = tree_algo.predict([listforinputsymptoms])
        final_disease = disease[y_pred[0]]

        return render(request, 'Results.html', {
            "name": pname,
            "symptoms": symptoms_selected,
            "disease": final_disease
        })

    return render(request, 'divyadrishti.html', {"Symptoms": symp_objs})


def get_bounds(lat, lon, radius_km):
    R = 6371  # Radius of Earth in km
    lat_rad, lon_rad = radians(lat), radians(lon)
    dlat, dlon = radius_km / R, radius_km / (R * cos(lat_rad))

    return (
        lat - degrees(dlat),
        lat + degrees(dlat),
        lon - degrees(dlon),
        lon + degrees(dlon)
    )


def distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * asin(sqrt(a)) * 6371  # Radius of Earth in km


def get_hospitals_within_radius(lat, lon, radius_km):
    min_lat, max_lat, min_lon, max_lon = get_bounds(lat, lon, radius_km)
    return Hospitals.objects.filter(
        latitude__gte=min_lat, latitude__lte=max_lat,
        longitude__gte=min_lon, longitude__lte=max_lon
    )


def table(request):
    lat, lon = map(lambda x: float(request.GET.get(x, None)), ['latitude', 'longitude'])
    finallist = get_hospitals_within_radius(lat, lon, radius_km=25) if lat and lon else []
    return render(request, 'table.html', {"hospitalList": finallist})


def get_client_ip(request):
    ip = request.META.get('HTTP_X_REAL_IP') or request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0]
    return ip if ip and not any(ip.startswith(prefix) for prefix in ['10.', '192.168', '172.']) else None


def get_location_by_ip(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
        if data.get('bogon'):
            return {'ip': ip, 'error': 'Bogon IP address, cannot determine location'}
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
        return JsonResponse({'error': 'Unable to determine public IP address.'})
    location = get_location_by_ip(ip)
    return JsonResponse(location)


def debug_headers_view(request):
    headers = {
        'X-Forwarded-For': request.META.get('HTTP_X_FORWARDED_FOR'),
        'X-Real-IP': request.META.get('HTTP_X_REAL_IP'),
        'Remote-Addr': request.META.get('REMOTE_ADDR'),
    }
    return JsonResponse(headers)