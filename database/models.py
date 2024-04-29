# models.py (in each app)

from django.db import models


        
class Patient(models.Model):
  patient_id = models.CharField(max_length=20, primary_key=True)  # Unique identifier for patient
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField()  # Stores patient's date of birth
  phone_number = models.CharField(max_length=15)  # Phone number for contact
  emergency_contact = models.CharField(max_length=100, blank=True)  # Optional emergency contact info
 
  def __str__(self):
    return f"{self.last_name}, {self.first_name} ({self.patient_id})"
    
class Staff(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True, null=True)
   

    def __str__(self):
        return f"{self.name} - {self.position} ({self.department})"
 
class Prescription(models.Model):
    patient_id = models.CharField(max_length=20)
    medications = models.TextField()
    lab_tests = models.TextField()
    dosage_instructions = models.TextField()
    
    def __str__(self):
        return f"Prescription for Patient ID: {self.patient_id}"
        
        
class Medication(models.Model):
    med_id = models.AutoField(primary_key=True)
    patient_id = models.CharField(max_length=20)
    medications = models.TextField()
    

    def __str__(self):
        return f"Medication ID: {self.med_id}, Patient ID: {self.patient_id}, Medications: {self.medications}"
        
        
class LabTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return f"Lab Test: {self.name}"
