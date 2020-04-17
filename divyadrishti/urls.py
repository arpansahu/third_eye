from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import view

urlpatterns = [
    path('', view.divyadrishti),
    path("table", view.table)
]
