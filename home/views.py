from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import csv
# Create your views here.


def export_to_csv(request):
    profiles = Customer.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename="customersData.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Balance'])
    profile_fields = profiles.values_list('name', 'balance')
    for profile in profile_fields:
        writer.writerow(profile)
    return response
    