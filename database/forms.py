from django import forms
from .models import Patient, Staff, Prescription, Medication, LabTest

class PatientForm(forms.ModelForm):
    node_choices = [
        ('node1', 'South'),
        ('node2', 'East'),
        ('node3', 'Central'),
    ]
    node = forms.ChoiceField(choices=node_choices)
    class Meta:
        model = Patient
        fields = '__all__'

class StaffForm(forms.ModelForm):
    node_choices = [
        ('node1', 'South'),
        ('node2', 'East'),
        ('node3', 'Central'),
    ]
    node = forms.ChoiceField(choices=node_choices)
    class Meta:
        model = Staff
        fields = '__all__'



class MedicationForm(forms.ModelForm):
    node_choices = [
        ('node1', 'South'),
        ('node2', 'East'),
        ('node3', 'Central'),
    ]
    node = forms.ChoiceField(choices=node_choices)
    class Meta:
        model = Medication
        fields = '__all__'


class LabTestForm(forms.ModelForm):
    node_choices = [
        ('node1', 'South'),
        ('node2', 'East'),
        ('node3', 'Central'),
    ]
    node = forms.ChoiceField(choices=node_choices)
    class Meta:
        model = LabTest
        fields = '__all__'



class PrescriptionForm(forms.ModelForm):
    node_choices = [
        ('node1', 'South'),
        ('node2', 'East'),
        ('node3', 'Central'),
    ]
    node = forms.ChoiceField(choices=node_choices)
    class Meta:
        model = Prescription
        fields = '__all__'



