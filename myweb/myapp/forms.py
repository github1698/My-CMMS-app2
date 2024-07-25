from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Equipment, Workorder,Asset,Vendor, Consumable, Department, Mech_Consumable,MaintOfficers,Requisition, Head

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'



            
       
class RequisitionFormAdmin(ModelForm):
    is_complete=forms.BooleanField(required=True)
    class Meta:
        model=Requisition
        fields=('emanating_dept','requesting_officer','hod_consent','equipment','action_by','section','manager','manager','date_submitted','date_received','is_complete')
        labels={
            'emanating_dept':'Requesting unit',
           
            'requesting_officer':'Requesting Officer',
            'hod_consent':'HOD',
           
            'equipment':'Name of Equipment',
            'action_by':'Endorsed By',
            'section':'Section',
            'manager':'In-Charge',
            'date_submitted':'YYYY-MM-DD',
            'date_received':'Date Submitted',
            'is_complete':'',
           
            

        }
        widgets = {
            'emanating_dept':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requesting Department'}),
            'requesting_officer':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requesting Officer'}),
            'hod_consent':forms.TextInput(attrs={'class':'form-control','placeholder':'HOD Comment'}),
                        
            'equipment':forms.Select(attrs={'class':'form-control','placeholder':'manager'}),
            'action_by':forms.TextInput(attrs={'class':'form-control','placeholder':'Supervisor'}),
            'section':forms.TextInput(attrs={'class':'form-control','placeholder':'Section'}),
            'manager':forms.Select(attrs={'class':'form-control','placeholder':'manager'}),
            'date_submitted':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Submitted'}),
            'date_received':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Received'}),
            'is_complete':forms.BooleanField(),
            
                }
class RequisitionForm(ModelForm):
    is_complete=forms.BooleanField(required=True)
    class Meta:
        model=Requisition
        fields=('emanating_dept','requesting_officer','hod_consent','equipment','action_by','section','manager','date_submitted','date_received','is_complete')
        labels={
            'emanating_dept':'',
           
            'requesting_officer':' ',
            'hod_consent':'',
           
            'equipment':'',
            'action_by':'',
            'section':'Section',
            'manager':'Manager',
           
            'date_submitted':'YYYY-MM-DD',
            'date_received':'',
            'is_complete':'',
           
            

        }
        widgets = {
            'emanating_dept':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requesting Department'}),
            'requesting_officer':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requesting Officer'}),
            'hod_consent':forms.TextInput(attrs={'class':'form-control','placeholder':'HOD Comment'}),
                        
            'equipment':forms.Select(attrs={'class':'form-control','placeholder':'Equipment Type'}),
            'action_by':forms.TextInput(attrs={'class':'form-control','placeholder':'Supervisor'}),
            'section':forms.Select(attrs={'class':'form-control','placeholder':'Section'}),
            
            'date_submitted':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Submitted'}),
            'date_received':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Received'}),
            'is_complete':forms.BooleanField(),
            
                }
class EquipmentFormAdmin(ModelForm):
    is_complete=forms.BooleanField(required=True)
    class Meta:
        model=Requisition
        fields=('emanating_dept','requesting_officer','hod_consent','equipment','action_by','section','manager','manager','date_submitted','date_received','is_complete')
        labels={
            'emanating_dept':'',
           
            'requesting_officer':' ',
            'hod_consent':'',
           
            'equipment':'',
            'action_by':'',
            'section':'',
            'manager':'',
            'date_submitted':'YYYY-MM-DD',
            'date_received':'',
            'is_complete':'',
           
            

        }
        widgets = {
            'emanating_dept':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requesting Department'}),
            'requesting_officer':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requesting Officer'}),
            'hod_consent':forms.TextInput(attrs={'class':'form-control','placeholder':'HOD Comment'}),
                        
            'equipment':forms.Select(attrs={'class':'form-control','placeholder':'Equipment Type'}),
            'action_by':forms.TextInput(attrs={'class':'form-control','placeholder':'Supervisor'}),
            'section':forms.TextInput(attrs={'class':'form-control','placeholder':'Section'}),
            'manager':forms.Select(attrs={'class':'form-control','placeholder':'manager'}),
            'date_submitted':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Submitted'}),
            'date_received':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Received'}),
            'is_complete':forms.BooleanField(),
            
                }
    

            
       


            

class EquipmentForm(ModelForm):
    is_complete=forms.BooleanField(required=True)
    class Meta:
        model=Equipment
        fields=('name','model','location','activities','last_service','next_service','cost','is_complete','attendees')
        labels={
            'name':'',
            'model':'',
            'location':'',
            'activities':'',
            'last_service':'',
            'next_service':'',
            'cost':'',
            'is_complete':'',
            'attendees':'',
            
            
            

        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Equipment Name'}),
            'model':forms.TextInput(attrs={'class':'form-control','placeholder':'Equipment model'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),
            'activities':forms.Textarea(attrs={'class':'form-control','placeholder':'Activities required to be done'}),
            'last_service':forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            'next_service':forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            'cost':forms.NumberInput(attrs={'class':'form-control','placeholder':'Cost'}),
            'is_complete':forms.BooleanField(),
            'attendees':forms.Select(attrs={'class':'form-control','placeholder':'Attending Officer'}),
            
       
        }
   
class WorkorderForm(ModelForm):
    completed=forms.BooleanField(required=True)
    class Meta:
        model=Workorder
        fields=('requesting_unit','department','receiving_unit','date_received','completion_date','machine','attendees','completed')
        labels={
            'requesting_unit':'',
            'department':'',
            'receiving_unit':'',
            'date_received':'',
            'completion_date':'',
            'item_used'
            'machine':'',
            
            'attendees':'',
            'completed':'',
        

        }
        widgets = {
            'requesting_unit':forms.TextInput(attrs={'class':'form-control','placeholder':'Requesting Officer'}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Department'}),
            'receiving_unit':forms.TextInput(attrs={'class':'form-control','placeholder':'Receiving Unit'}),
            'date_received':forms.DateInput(attrs={'class':'form-control','placeholder':'Received Date YYYY-MM-DD'}),
            'completion_date':forms.DateInput(attrs={'class':'form-control','placeholder':'Completion Date YYYY-MM-DD'}),
            'machine':forms.TextInput(attrs={'class':'form-control','placeholder':'machines'}),
            
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attending Officer'}),
            'completed':forms.BooleanField(),
            
        }

class WorkorderFormAdmin(ModelForm):
    complete=forms.BooleanField(required=True)
    class Meta:
        model=Workorder
        fields=('requesting_unit','department','receiving_unit','date_received','completion_date','machine','item_used','completed')
        labels={
            'requesting_unit':'',
            'department':'',
            'receiving_unit':'',
            'date_received':'',
            'completion_date':'',
            'machine':'',
            'item_used':'',
            
            'attendees':'',
            'completed':'',
           

        }
        widgets = {
            'requesting_unit':forms.TextInput(attrs={'class':'form-control','placeholder':'Requesting Officer'}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Department'}),
            'receiving_unit':forms.TextInput(attrs={'class':'form-control','placeholder':'Receiving Unit'}),
            'date_received':forms.DateInput(attrs={'class':'form-control','placeholder':'Request Date'}),
            'completion_date':forms.DateInput(attrs={'class':'form-control','placeholder':'Completion Date'}),
            'machine':forms.TextInput(attrs={'class':'form-control','placeholder':'Machines'}),
            'item_used':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Consumables'}),
            
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attending Officer'}),
            'status':forms.TextInput(attrs={'class':'form-control','placeholder':'Completed/Not Completed'}),
            
        }

    
class AssetForm(ModelForm):
    class Meta:
        model=Asset
        fields=('asset_name','supply_date','model','quantity','asset_department','present_condition','comment')
        labels={
            'asset_name':'',
            'supply_date':'',
            'model':'',
            'quantity':'',
            'asset_department':'',
            'present_condition':'',
            'comment':'',

        }
        widgets = {
            'asset_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset name'}),
            'supply_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Supplied'}),
            'model':forms.TextInput(attrs={'class':'form-select','placeholder':'Model'}),
            'quantity':forms.TextInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'asset_department':forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),
            'present_condition':forms.Textarea(attrs={'class':'form-control','placeholder':'Present Condition'}),
            'comment':forms.Textarea(attrs={'class':'form-control','placeholder':'General Comment'}),
        }
        

class ConsumableForm(ModelForm):
    class Meta:
        model=Consumable
        fields=('item_name','quantity','issued_quantity','received_by','issued_by','issued_to','balance','phone_number','reorder_level','last_updated','timestamp')
        labels={
            'item_name':'Consumable Name',
            'quantity':'Quantity',
            'issued_quantity':'Quantity',
            'received_by':'Receiving Officer',
            'issued_by':'Issuing Officer',
            'issued_to':'',
            'balance':'Balance',
            'phone_number':'Phone Number',
            
            'reorder_level':'Reorder',
            'last_updated':'',
            'timestamp':'',

        }
        
        widgets = {
            'item_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Consumable name'}),
            'quantity':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Supplied'}),
            'issued_quantity':forms.TextInput(attrs={'class':'form-select','placeholder':'Model'}),
            'received_by':forms.TextInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'issued_by':forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),
            'issued_to':forms.TextInput(attrs={'class':'form-control','placeholder':'General Comment'}),
            'balance':forms.TextInput(attrs={'class':'form-control','placeholder':'General Comment'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Used'}),
            'reorder_level':forms.TextInput(attrs={'class':'form-control','placeholder':'Balance'}),
            'last_updated':forms.DateInput(attrs={'class':'form-control','placeholder':'Reorder Date'}),
            'timestamp':forms.DateInput(attrs={'class':'form-controlt','placeholder':' Manager'}),
            # 'Balance':forms.TextInput(attrs={'class':'form-control','placeholder':'Balance'}),
            # 'Reorder':forms.TextInput(attrs={'class':'form-control','placeholder':'Reorder'}),
           
        } 
       
class Mech_ConsumableForm(ModelForm):
    class Meta:
        model=Mech_Consumable
        fields=('name','type','unit','quantity')
        labels={
            'name':'',
            'type':'',
            'unit':'',
            'quantity':'',
           
            

        }
        widgets = {
            'consumable_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset name'}),
            'equipment_type':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Supplied'}),
            'unit':forms.TextInput(attrs={'class':'form-select','placeholder':'Model'}),
            'quantity':forms.TextInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),
            
        } 
class MaintOfficersForm(ModelForm):
    class Meta:
        model=MaintOfficers
        fields=('first_name','last_name','email')
        labels={
            'first_name':'',
            'last_name':'',
            'email':'',
            
           
            

        }
        widgets = {
            'consumable_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Asset name'}),
            'equipment_type':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Supplied'}),
            'unit':forms.TextInput(attrs={'class':'form-select','placeholder':'Model'}),
            'quantity':forms.TextInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),
            
        } 


class VendorForm(ModelForm):
    class Meta:
        model=Vendor
        fields=('name','address','zip_code','phone','web','email_address')
        labels={
            'name':'',
            'address':'',
            'zip_code':'',
            'phone':'',
            'web':'',
            'email_address':'',
            

        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Supplier name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Zip_code'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Web'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email_Address'}),
        }

class DepartmentForm(ModelForm):
    class Meta:
        model=Department
        fields=('department_name','appendage_name')
        labels={
            'department_name':'',
            'appendage_name':'',
           
            

        }
        widgets = {
            'department_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Store_outlet name'}),
            'appendage_name':forms.TextInput(attrs={'class':'form-select','placeholder':'Supplier'}),
        }


class MaintOfficersForm(ModelForm):
    class Meta:
        model=MaintOfficers
        fields=('first_name','last_name')
        labels={
            'first_name':'',
            'last_name':'',
           
            

        }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Store_outlet name'}),
            'last_name':forms.TextInput(attrs={'class':'form-select','placeholder':'Supplier'}),
        }
class HeadForm(ModelForm):
    class Meta:
        model=Head
        fields=('first_name','last_name')
        labels={
            'first_name':'',
            'last_name':'',
           
            

        }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Store_outlet name'}),
            'last_name':forms.TextInput(attrs={'class':'form-select','placeholder':'Supplier'}),
        }