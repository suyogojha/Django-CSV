from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Customer
from django.urls import path
from django.shortcuts import redirect, render
from django import forms
from django.contrib import messages
# Register your models here.

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField() 





class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')
    
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls   

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'THIS IS NOT A CSV FILE')
                return HttpResponseRedirect(request.path_info)
            
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            for x in csv_data:
                fields = x.split(",")
                created = Customer.objects.get_or_create(name=fields[0], balance=fields[1])
                return redirect("/admin/home/customer/")
            
        form = CsvImportForm()
        data = {"form": form}
        return render(request, 'admin/csv_upload.html', data)
    
    
admin.site.register(Customer, CustomerAdmin)