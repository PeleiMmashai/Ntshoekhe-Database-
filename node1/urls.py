from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowPatient, name='show_patient'),
    path('Create_record', views.create_record, name='Create_record'),
    path('Edit_record/<int:id>', views.Edit_record, name="Edit_record"),
    path('Update_record/<int:id>', views.Update_record, name="Update_record"),
    path('Delete_record/<int:id>/', views.Delete_record, name='Delete_record'),
]

