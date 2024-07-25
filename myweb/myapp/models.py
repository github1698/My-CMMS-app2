from django.db import models
from django.utils import timezone
from datetime import date
from datetime import datetime, timedelta
from time import strftime
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.urls import reverse
from jsignature.fields import JSignatureField


# class Activities(models.Model):
#     name=models.ForeignKey("MaintOfficers", blank=True, null=True, on_delete=models.SET_NULL)
#     date=models.DateField(date.today)
#     todo=models.TextField(max_length=500, blank=True, null=True)
#     status=models.CharField(max_length=30, default=False)
#     comments=models.TextField(max_length=500, blank=True, null=True)
#     section=models.CharField(max_length=50, default=None)
#     sub_unit=models.CharField(max_length=50, default=None)
#     complete=models.BooleanField(default=False)
#     department=models.ForeignKey('Department',blank=True, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#          return self.department

class Requisition(models.Model):
    emanating_dept=models.CharField(max_length=200, blank = True, null = True,default='')
    requesting_officer=models.TextField('In_Charge',max_length=500, blank=True, null=True)
    hod_consent=models.CharField(max_length=30)
    equipment=models.ForeignKey('Equipment',blank=True, null=True, on_delete=models.SET_NULL)
    action_by=models.CharField(max_length=200, blank = True, null = True,default='')
    sub_unit=models.ForeignKey('Sub_unit',blank=True, null=True, on_delete=models.SET_NULL)
    section=models.ForeignKey('Section',blank=True, null=True, on_delete=models.SET_NULL)
    manager=models.ForeignKey('Manager',blank=True, null=True, on_delete=models.SET_NULL)
    date_submitted=models.DateTimeField(blank=True, null=True)
    date_received=models.DateTimeField(blank=True, null=True)
    is_complete=models.BooleanField(default=False)
    request_image=models.ImageField(null=True, blank=True, upload_to="images/")
    

    def __str__(self):
       return self.emanating_dept
    @property
    def name(self):
        return self.action_by.first_name
    @property
    def name(self):
        return self.action_by.dept
class Category(models.Model):
    name=models.CharField(max_length=50,blank=True, null=True)
    
    def __str__(self):
       return self.name
    
class Consumable(models.Model):
    item_name=models.CharField(max_length=50,blank=True, null=True, default="")
    department=models.ForeignKey("Department", blank=True, null=True, on_delete=models.SET_NULL)
    quantity=models.IntegerField(default='0',blank=True, null=True)
    issued_quantity=models.IntegerField(default='0',blank=True, null=True)
    received_by=models.CharField(max_length=50,blank=True, null=True)
    issued_by=models.CharField(max_length=50,blank=True, null=True)
    issued_to=models.CharField(max_length=50,blank=True, null=True)
    balance=models.IntegerField(default='0',blank=True, null=True)
    phone_number=models.CharField(max_length=50,blank=True, null=True)
    reorder_level=models.IntegerField(default='0',blank=True, null=True)
    last_updated=models.DateTimeField(blank=True, null=True)
    manager=models.CharField(max_length=50,blank=True, null=True, default="")
    timestamp=models.DateTimeField(blank=True, null=True) 

    def __str__(self):
        return self.item_name
        
        
    
    @property
    def Balance(self):
        balanced=self.quantity-self.issued_quantity
        self.balance=balanced
        return self.balance

    
    @property
    def Reorder(self):
        
        if self.balance==1/5*self.quantity:
            
            return f'pls reorder {self.quantity}'
    



class Equipment(models.Model):
    name=models.CharField(max_length=50, default="")
    model=models.CharField(max_length=50, default="", null=True, blank=True)
    location=models.CharField(max_length=70, default="",null=True, blank=True)
    activities=models.TextField(max_length=300,null=False,blank=False,default='')
    last_service=models.DateTimeField(blank=True, null=True,default="")
    next_service=models.DateTimeField(blank=True, null=True,default="")
    cost=models.FloatField(blank=True, null=True)
    is_complete=models.BooleanField(default=False)
    attendees=models.ForeignKey("MaintOfficers", blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name
    
    @property
    def Next_date(self):
        today=date.today()
        next_date=self.last_service.date()-today
        next_date_stripped=str(next_date).split(",",1)
        return next_date_stripped
    @property
    def is_past(self):
        today=date.today()
        if self.last_service.date()>today:
            thing='past'
        else:
            thing='future'
        return thing
     

class Workorder(models.Model):
    requesting_unit=models.CharField( max_length=50)
    department=models.CharField(max_length=50)
    receiving_unit=models.CharField(max_length=50)
    date_received=models.DateField(date.today)
    completion_date=models.DateTimeField(default=timezone.now)
    machine=models.CharField(max_length=250, default='')
    item_used=models.ForeignKey("Consumable", blank=True, null=True, on_delete=models.SET_NULL)
    attendees=models.ManyToManyField('MaintOfficers', blank=True)
    completed=models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.requesting_unit
    @property
    def Day_till(self):
        today=date.today()
        day_till=self.date_received.date()-today
        stripped_day_till=str(day_till).split(",",1)[0]
        return stripped_day_till
    

    def Is_past(self):
        today=date.today()
        if self.date_received.date()>today:
            thing="past"
        else:
            thing="Future"
        return thing

class Manager(models.Model):
    name=models.CharField( max_length=120)
    department=models.CharField( max_length=120)
    
    def __str__(self):
        return self.name
    
    
class Asset(models.Model):
    asset_name=models.CharField( max_length=120)
    supply_date=models.DateField(date.today)
    model=models.CharField(max_length=20)
    quantity=models.IntegerField(blank=True, null=True)
    asset_department=models.CharField(max_length=50)
    present_condition=models.CharField(max_length=50)
    comment=models.TextField(max_length=500, blank=True, null=True)
    owner=models.IntegerField(blank=False, default=1)
    asset_image=models.ImageField(null=True, blank=True, upload_to="images/")
    

    def __str__(self):
        return self.asset_name
    
# class Consumable(models.Model):
#     consumable_name=models.CharField( max_length=120)
#     equipment_type=models.ForeignKey("Equipment",blank=True, null=True, on_delete=models.DO_NOTHING)
#     unit=models.CharField(max_length=30)
#     quantity=models.IntegerField(blank=True, null=True)
#     location=models.CharField(max_length=50)
#     comment=models.TextField(max_length=500, blank=True, null=True)
#     department=models.CharField(max_length=50, default=0)
#     used=models.IntegerField(blank=False, null=False, default=0)
#     balance = models.IntegerField(default=0, null=True, blank=True)
#     due_date=models.DateField(date.today)
#     #due_date=models.DateTimeField(default=timezone.now, null=True)
#     manager=models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
#     consumable_image=models.ImageField(null=True, blank=True, upload_to="images/")
    
    
#     def __str__(self):
#         return self.consumable_name
    

    # def save(self, *args, **kwargs):
    #         self.balance =  self.quantity-self.used
    #         self.due_date = datetime.now()+timedelta(days=30)
    #         return datetime.now().strftime('%Y')
    
class Mech_Consumable(models.Model):
    name=models.CharField( max_length=120)
    type=models.ForeignKey("Equipment",blank=True, null=True, on_delete=models.SET_NULL)
    unit=models.CharField(max_length=30)
    quantity=models.IntegerField(blank=True, null=True)
    
    
    def __str__(self):
        return self.name

class Vendor(models.Model):
    name=models.CharField('Supplier name', max_length=120)
    address=models.CharField(max_length=250)
    zip_code=models.CharField('Zip code', max_length=20, blank=True)
    phone=models.CharField('Phone no', max_length=30)
    web=models.URLField('Website Address', blank=True)
    email_address=models.EmailField('Email Address',blank=True)
    owner=models.IntegerField(blank=False, default=1)
    venue_image=models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self): 
        return self.name

def one_week_hence():
    return timezone.now() +timezone.timedelta(days=1)

class TodoList(models.Model):
    title=models.CharField(max_length=150, unique=True)
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    def __str__(self): 
        return self.title
    
class TodoItem(models.Model):
   title=models.CharField(max_length=150)
   description=models.TextField(null=True, blank=True)
   created_date=models.DateTimeField(auto_now_add=True)
   due_date=models.DateTimeField(default=one_week_hence)
   todo_list=models.ForeignKey(TodoList, on_delete=models.CASCADE)
   
   def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])
    
   def __str__(self): 
        return f"(self.title): due{self.due_date})"
    
class Meta:
    ordering=['due_date']
    

class WorkDoneList(models.Model):
    title=models.ForeignKey(Workorder, default='', on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("work", args=[self.id])
    
    def __str__(self): 
        return self.title
class WorkDoneItem(models.Model):
   title=models.CharField(max_length=150)
   department=models.CharField(max_length=150)
   name=models.TextField(null=True, blank=True)
   completed_date=models.DateTimeField(auto_now_add=True)
   delivery_date=models.DateTimeField(default=one_week_hence)
   work_list=models.ForeignKey(WorkDoneList, default='', on_delete=models.CASCADE)
   cost=models.CharField(max_length=150)
   
   def get_absolute_url(self):
        return reverse("work-update", args=[str(self.work_list.id), str(self.id)])
    
   def __str__(self): 
        return f"(self.title): due{self.delivery_date})"
    
class Meta:
    ordering=['delivery_date']
    
class Department(models.Model):
    department_name=models.CharField('Department name', max_length=45)
    appendage_name=models.CharField('Appendage', max_length=40, default='None')
   

   
    def __str__(self):
        return (self.department_name + ' ' + self.appendage_name)

    

class MaintOfficers(models.Model):
    first_name=models.CharField('First name', max_length=45)
    last_name=models.CharField('Last name', max_length=40)
    email=models.EmailField('User Email', blank=True)

    def __str__(self):
       return str(self.first_name) 
    
class Head(models.Model):
    first_name=models.CharField('First name', max_length=45)
    last_name=models.CharField('Last name', max_length=40)
    dept=models.CharField('department', max_length=45)

    def __str__(self):
       return str(self.first_name) 
    
class Activities(models.Model):
    todo=models.CharField(max_length=500, blank=True, null=True)
    todo_date=models.DateTimeField(blank=True, null=True)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.todo
    
class Section(models.Model):
    unit=models.CharField(max_length=500, blank=True, null=True)
    department1=models.DateTimeField(blank=True, null=True)
   

    def __str__(self):
        return self.unit


class Sub_unit(models.Model):
    unit=models.CharField(max_length=500, blank=True, null=True)
    section=models.DateTimeField(blank=True, null=True)
   

    def __str__(self):
        return self.unit
    
class SignatureModel(models.Model):
    signature = JSignatureField()
   


