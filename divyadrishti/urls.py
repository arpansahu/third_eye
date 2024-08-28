from django.contrib import admin
from django.urls import path

from . import view

urlpatterns = [
    path('', view.divya_drishti),
    path("table", view.table, name='table'),
    path("location", view.user_location_view),
    path("headers", view.debug_headers_view),
]
