from django.shortcuts import render
from node1.models import Patient
from django.contrib import messages
from node1.forms import PatientForm

def ShowPatient(request):
    showall = Patient.objects.all()
    return render(request, 'index.html', {'data': showall})///////////////////////////////////////

def create_record(request):
    if request.method == "POST":
        if (
            request.POST.get('patient_id') and
            request.POST.get('first_name') and
            request.POST.get('last_name') and
            request.POST.get('date_of_birth') and
            request.POST.get('phone_number') and
            request.POST.get('emergency_contact')
        ):
            saverecord = Patient()
            saverecord.patient_id = request.POST.get('patient_id')
            saverecord.first_name = request.POST.get('first_name')
            saverecord.last_name = request.POST.get('last_name')
            saverecord.date_of_birth = request.POST.get('date_of_birth')
            saverecord.phone_number = request.POST.get('phone_number')
            saverecord.emergency_contact = request.POST.get('emergency_contact')
            saverecord.save()
            messages.success(request, 'Patient ' + saverecord.first_name + ' ' + saverecord.last_name + ' is saved successfully...!')
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

def Edit_record(request, id):
    edite_record_obj=Patient.objects.get(id=id)
    return render(request, 'edit.html', {"Patient": edite_record_obj})

def Update_record(request, id):
    Update_record=Patient.objects.get(id=id)
    form=PatientForms(request.POST, instance=Update_record)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully...!')
        return render(request, 'edit.html', {"Patient": Update_record})
    
def Delete_record(request, id):
    delete_record=Patient.objects.get(id=id)
    delete_record.delete()
    showdata=Patient.objects.all()
    return render(request, "index.html", {"data":showdata})
