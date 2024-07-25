from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from datetime import datetime
from . models import Workorder,Equipment,Vendor,Consumable,Asset, Requisition, Equipment, Activities
from .forms import VendorForm, WorkorderForm, WorkorderFormAdmin,EquipmentForm, ConsumableForm,AssetForm, RequisitionForm,RequisitionFormAdmin, MaintOfficersForm, HeadForm,SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import FileResponse
import io
import requests
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.mail import send_mail
#import pagination stuff
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoList, TodoItem, WorkDoneList,WorkDoneItem
from django.urls import reverse,reverse_lazy



def workorder_pdf(request):
      #create Bytestream buffer
      buf=io.BytesIO()
      #create canvas
      c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
      #create text object
      textob=c.beginText()
      textob.setTextOrigin(inch, inch)
      textob.setFont("Helvetica", 14)

      #craete lines
      #lines=[
       #     'This is line 1',
        #    'This is line 2',
         #   'This is line 3',
     # ]
      workorders=Workorder.objects.all()

      lines=[]

      for workorder in workorders:
            lines.append(workorder.requesting_unit)
            lines.append(workorder.department)
            lines.append(workorder.equipment)
            lines.append(workorder.date_received)
            lines.append(workorder.completion_date)
            lines.append(workorder.status)
            lines.append('')
            
            
            

      for line in lines:
            textob.textLine(line)
            
      c.drawText(textob)
      c.showPage()
      c.save()
      buf.seek(0)

      return FileResponse(buf, as_attachment=True, filename='workorder_pdf')

      response=HttpResponse(content_type='text/csv')
      response['content-disposition']='attachment; filename=vendor.csv'

def activitieslist_pdf(request):
      #create Bytestream buffer
      buf=io.BytesIO()
      #create canvas
      c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
      #create text object
      textob=c.beginText()
      textob.setTextOrigin(inch, inch)
      textob.setFont("Helvetica", 14)

      #craete lines
      #lines=[
       #     'This is line 1',
        #    'This is line 2',
         #   'This is line 3',
     # ]
      activities=Requisition.objects.all()

      lines=[]

      for activity in activities:
            lines.append(activity.name)
           # lines.append(activity.date)
            lines.append(activity.activity)
            lines.append(activity.status)
            lines.append(activity.text)
            lines.append(activity.section)
            lines.append(activity.sub_unit)
            lines.append(activity.complete)
            lines.append('')
            
            
            

      for line in lines:
            textob.textLine(line)
            
      c.drawText(textob)
      c.showPage()
      c.save()
      buf.seek(0)

      return FileResponse(buf, as_attachment=True, filename='workorder_pdf')

      response=HttpResponse(content_type='text/csv')
      response['content-disposition']='attachment; filename=vendor.csv'

def activitieslist_csv(request):
      response=HttpResponse(content_type='text/csv')
      response['content-disposition']='attachment; filename=workorder.csv'
      
      #to establish the column
      writer=csv.writer(response)
      activities=Requisition.objects.all()

      writer.writerow(['Activity name','Activity date','activity activity','activity status','activity secton', 'Manager','approved'])

      
      for activity in activities:
            writer.writerow(['activity.name','activity.date','activity.active','activity.status','activity.text','activity.section','activity.sub_unit','activity.complete'])
      
      return response
#let generate text file
def workorder_csv(request):
      response=HttpResponse(content_type='text/csv')
      response['content-disposition']='attachment; filename=workorder.csv'
      
      #to establish the column
      writer=csv.writer(response)
      workorders=Workorder.objects.all()

      writer.writerow(['Workorder Unit','Workorder equipment','Workorder department','Workorder completion_date','Manager','approved'])

      
      for workorder in workorders:
            writer.writerow([workorder.requesting_unit,workorder.equipment,workorder.department,workorder.completion_date,workorder.manager,workorder.status])
      
      return response
#let generate text file
def workorder_csv(request):
      response=HttpResponse(content_type='text/csv')
      response['content-disposition']='attachment; filename=workorder.csv'
      
      #to establish the column
      writer=csv.writer(response)
      workorders=Workorder.objects.all()

      writer.writerow(['Workorder Unit','Workorder equipment','Workorder department','Workorder completion_date','Manager','approved'])

      
      for workorder in workorders:
            writer.writerow([workorder.requesting_unit,workorder.equipment,workorder.department,workorder.completion_date,workorder.manager,workorder.status])
      
      return response
#let generate text file
def workorder_text(request):
      response=HttpResponse(content_type='text/plain')
      response['content-disposition']='attachment; filename=workorder.txt'
      
      workorders=Workorder.objects.all()

      lines=[]

      for workorder in workorders:
            lines.append(f"{workorder.requesting_unit}\n{workorder.equipment}\n{workorder.department}\n{workorder.completion_date}\n{workorder.manager}\n{workorder.status}\n\n\n")
     
      response.writelines(lines)
      return response
def activitieslist_text(request):
      response=HttpResponse(content_type='text/plain')
      response['content-disposition']='attachment; filename=workorder.txt'
      
      activities=Requisition.objects.all()

      lines=[]

      for activity in activities:
            lines.append(f"{activity.name}\n{activity.date}\n{activity.activity}\n{activity.status}\n{activity.text}\n{activity.section}\n{activity.sub_unit}\n{activity.complete}\n\n\n")
      
      response.writelines(lines)
      return response

def done_page(request):
    phone = request.GET.get('phone')
    text = request.GET.get('text')

    return render(request, "en/done.html" , {'phn':phone , 'txt':text})

def sendPostRequest( req_URL ,API_key , secret_API , text_message , phone_no , sender):

    req_param = {
        'apikey' : API_key, 
        'secretKey' :secret_API, 
        'message' :text_message ,
        'phone' :phone_no, 
        'from': sender,   
    }

    #return requests.post(req_URL , req_param)

def done_page(request):
    phone = request.GET.get('phone')
    text = request.GET.get('text')

    t_phone = 'numbers='+ f'{phone}' + '&'
    t_text = 'message=' + f'{text}' + '&'
 
    # get resposnse 
    sendPostRequest(
        URL ,'username=XXXXXX' , 'password=XXXXXXX' , t_text
        , t_phone,'sender=Matager&unicode=e&Rmduplicated=0&return=Json')
    return render(request, "en/done.html" , {'phn':phone , 'txt':text})

class ListListView(ListView):
    model=TodoList
    template_name='myapp/todo.html'
    
class ItemListView(ListView):
    model=TodoItem
    template_name='myapp/todo_list.html'
    
    def get_queryset(self):
         return TodoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
     
    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = TodoList.objects.get(id=self.kwargs['list_id'])
        return context
class ListCreate(CreateView):
    model=TodoList
    fields=['title']
    
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context
    
    # def get_context_data(self):
    #      context = super().get_context_data()
    #      context["todo_list"] = TodoList.objects.get(id=self.kwargs['list_id'])
    #      return context
class ItemCreate(CreateView):
    model=TodoItem
    fields=[
        'todo_list',
        'title',
        'description',
        'due_date',
        
            ]
    def get_initial(self):
        initial_data=super(ItemCreate, self).get_initial()
        todo_list=TodoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list']=todo_list
        return initial_data
    
    def get_context_data(self):
        context=super(ItemCreate, self).get_context_data()
        todo_list= TodoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list']=todo_list
        context['title']= 'Create a new item'
        return context
         
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])
    
class ItemUpdate(UpdateView):
    model=TodoItem
    fields=['todo_list',
            'title',
            'description',
            'due_date',]
    
    def get_context_data(self):
        context= super(ItemUpdate, self).get_context_data()
        context['todo_list']= self.object.todo_list
        context['title']='Edit item'
        return context
        
    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])

class ListDelete(DeleteView):
    model=TodoList
    #use reverse_lazy() instead of reverse()
    #as the urls are not loaded when the file s imported
    success_url=reverse_lazy('to-do')
    
class ItemDelete(DeleteView):
    model=TodoItem
    
    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs['list_id']])  
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs) 
        context['todo_list']= self.object.todo_list 
        return context


def delete_equipment(request, equipment_id):
    equipment=Equipment.objects.get(pk=equipment_id)
    if request.user == equipment.manager:
        equipment.delete()
        messages.success(request, ('page deleted successfully'))
        return redirect('equipment')

    else:
        messages.success(request, ('You are not permitted to delete this page'))

def delete_consumable(request, consumable_id):
      consumable=Consumable.objects.get(pk=consumable_id)
      consumable.delete()
      messages.success(request, ('page deleted successfully'))
      return redirect('consumable-list')

     

def delete_asset(request, asset_id):
      asset=Asset.objects.get(pk=asset_id)
      asset.delete()
      messages.success(request, ('page deleted successfully'))
      return redirect('asset-list')


def delete_Vendor(request, vendor_id):
    vendor=Vendor.objects.get(pk=vendor_id)
    vendor.delete()
    messages.success(request, ('page deleted successfully'))
    return redirect('list-vendor')

def delete_request(request, requisition_id):
    requisition=Requisition.objects.get(pk=requisition_id)
    requisition.delete()
    messages.success(request, ('page deleted successfully'))
    return redirect('all-requests')

def delete_workorder(request, workorder_id):
    workorder=Workorder.objects.get(pk=workorder_id)
    #if request.user == workorder.manager:
    workorder.delete()
    messages.success(request, ('page deleted successfully'))
    return redirect('all-workorder')

   # else:
        #messages.success(request, ('You are not permitted to delete this page'))



def update_consumable(request, consumable_id):
      consumable=Consumable.objects.get(pk=consumable_id)
      form=ConsumableForm(request.POST or None, request.FILES or None, instance=consumable)
      if form.is_valid():
            form.save()
            return redirect('consumable-list')
      
      return render(request,"myapp/update_consumable.html",{
            "consumable":consumable, "form":form
      })
def update_equipment(request, equipment_id):
      equipment=Equipment.objects.get(pk=equipment_id)
      form=EquipmentForm(request.POST or None, request.FILES or None, instance=equipment)
      if form.is_valid():
            form.save()
            return redirect('equipment-list')
      
      return render(request,"myapp/update_equipment.html",{
            "equipment":equipment, "form":form
      })

def update_vendor(request, vendor_id):
      vendor=Vendor.objects.get(pk=vendor_id)
      form=VendorForm(request.POST or None, request.FILES or None, instance=vendor)
      if form.is_valid():
            form.save()
            return redirect('list-vendor')
      
      return render(request,"myapp/update_vendor.html",{
            "vendor":vendor, "form":form
      })
def update_request(request, requisition_id):
    update_request=Requisition.objects.get(pk=requisition_id)
    form=RequisitionFormAdmin(request.POST or None, request.FILES or None, instance=update_request)
    if form.is_valid():
        form.save()
        return redirect('all-requests')
      
    return render(request,"myapp/update_request.html",
        {"update_request":update_request, "form":form
      })
      
def search_vendor(request):
      if request.method=="POST":
            searched=request.POST['searched']
            vendors=Vendor.objects.filter(name__contains=searched)
            return render(request,"myapp/search_vendor.html",{
                  "searched":searched, "vendors":vendors
            })
      
      else: 
            return render(request,"myapp/search_vendor.html",{})
      
def show_consumable(request, consumable_id):
      consumable=Consumable.objects.get(pk=consumable_id)
      #figure=consumable.Balance()
      
      #vendor_owner=User.objects.get(pk=vendor.owner)
      return render(request,"myapp/show_consumable.html",{
            "consumable":consumable, 
      })    
      
def show_asset(request, asset_id):
    asset=Asset.objects.get(pk=asset_id)
      #vendor_owner=User.objects.get(pk=vendor.owner)
    return render(request,"myapp/show_asset.html",{
            "asset":asset
      })    
def show_equipment(request, equipment_id):
    equipment=Equipment.objects.get(pk=equipment_id)
      #vendor_owner=User.objects.get(pk=vendor.owner)
    return render(request,"myapp/show_equipment.html",{
            "equipment":equipment
      })    

def show_vendor(request, vendor_id):
    vendor=Vendor.objects.get(pk=vendor_id)
    vendor_owner=User.objects.get(pk=vendor.owner)
    return render(request,"myapp/show_vendor.html",{
            "vendor":vendor,'vendor_owner':vendor_owner
      })
def show_request(request,requisition_id):
    requisition=Requisition.objects.get(pk=requisition_id)
      #activity_owner=User.objects.get(pk=activity.owner)
    return render(request,"myapp/show_request.html",{
            "requisition":requisition
      })

def show_Workorder(request,workorder_id):
    workorder=Workorder.objects.get(pk=workorder_id)
    workorder_owner=User.objects.get(pk=workorder.owner)
    return render(request,"myapp/show_workorder.html",{
            "workorder":workorder,'workorder_owner':workorder_owner
      })
def show_asset(request,asset_id):
    asset=Asset.objects.get(pk=asset_id)
    asset_owner=User.objects.get(pk=asset.owner)
    return render(request,"myapp/show_asset.html",{
            "asset":asset,'asset_owner':asset_owner
      })
def list_request(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    requisitions = Requisition.objects.all()
    return render(request,'myapp/request_list.html', {
            "requisitions":requisitions
      }) 
def asset_list(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    assets = Asset.objects.all()
    return render(request,'myapp/asset_list.html', {
            "asssts":assets
      }) 
def list_equipment(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    equipments = Equipment.objects.all()
    return render(request,'myapp/equipment_list.html', {
            "equipments":equipments
      }) 

def list_vendor(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    vendors = Vendor.objects.all()
    return render(request,'myapp/vendor_list.html', {
            "vendors":vendors
      }) 
def add_consumable(request):
    
    submitted=False
    if request.method=='POST':
        form=ConsumableForm(request.POST)
        if form.is_valid():
            consumable=form.save(commit = False)
            consumable.save()
        
         
            return HttpResponseRedirect('/add_consumable? submitted=True',{
                        "form":form})
    else:
        form=ConsumableForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"myapp/add_consumable.html",{"form":form,'submitted':submitted})  

def add_equipment(request):
    submitted=False
    if request.method=='POST':
        form=EquipmentForm(request.POST)
        if form.is_valid():
            equipment=form.save(commit = False)
            equipment.save()
         
            return HttpResponseRedirect('/add_equipment? submitted=True',{
                        "form":form})
    else:
        form=EquipmentForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"myapp/add_equipment.html",{"form":form,'submitted':submitted})                  

def add_vendor(request):
    submitted=False
    if request.method=='POST':
        form=VendorForm(request.POST)
        if form.is_valid():
            vendor=form.save(commit = False)
            vendor.save()
         
            return HttpResponseRedirect('/add_vendor? submitted=True',{
                        "form":form})
    else:
        form=VendorForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"myapp/add_vendor.html",{"form":form,'submitted':submitted})
             
def add_workorder(request):
    submitted=False
    if request.method=='POST':
        form=WorkorderForm(request.POST)
        if form.is_valid():
            workorder=form.save(commit = False)
            workorder.save()
            email_add(request)
            return HttpResponseRedirect('/add_workorder? submitted=True',{
                        "form":form})
    else:
        form=WorkorderForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"myapp/add_workorder.html",{"form":form,'submitted':submitted})

def add_request(request):
    submitted=False
    if request.method=='POST':
        form=RequisitionForm(request.POST)
        if form.is_valid():
            requisition=form.save(commit = False)
            requisition.save()
            sendSmS()
            return HttpResponseRedirect('/add_request? submitted=True',{
                        "form":form})
    else:
        form=RequisitionForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"myapp/add_request.html",{"form":form,'submitted':submitted})
             
def add_asset(request):
    submitted=False
    if request.method=='POST':
        form=AssetForm(request.POST)
        if form.is_valid():
            asset=form.save(commit = False)
            asset.save()
         
            return HttpResponseRedirect('/add_asset? submitted=True',{
                        "form":form})
    else:
        form=AssetForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"myapp/add_asset.html",{"form":form,'submitted':submitted})

def add_equipment(request):
    submitted=False
    if request.method=='POST':
        form=EquipmentForm(request.POST)
        if form.is_valid():
            equipment=form.save(commit = False)
            equipment.save()
         
            return HttpResponseRedirect('/add_equipment? submitted=True',{
                        "form":form})
    else:
        form=EquipmentForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"myapp/add_equipment.html",{"form":form,'submitted':submitted})
             
             
      


def Consumables(request):
     # supplier_list = Supplier.objects.all().order_by('name')
      consumable_list = Consumable.objects.all()
     
      p=Paginator(Consumable.objects.all(), 4)
      page=request.GET.get('page')
      consumables=p.get_page(page)
      nums="a"*consumables.paginator.num_pages

      return render(request,'myapp/consumable.html', {
            "consumable_list":consumable_list, 'consumables':consumables, "nums":nums
      })       

def mechanical_consumable(request):
    # 1st solution
    mech_consumable = Consumable.objects.filter(
        department='1')
    # This command will retrieve indians nationality peoples
    return render(request, 'myapp/mech_consumable.html',
                  {'mech_consumable': mech_consumable})

def electrical_consumable(request):
    # 1st solution
    elect_consumable = Consumable.objects.filter(
        department='2')
    # This command will retrieve indians nationality peoples
    return render(request, 'myapp/elect_consumable.html',
                  {'elect_consumable': elect_consumable})

def biomedical_consumable(request):
    # 1st solution
    bio_consumable = Consumable.objects.filter(
        department='3')
    # This command will retrieve indians nationality peoples
    return render(request, 'myapp/bio_consumable.html',
                  {'bio_consumable': bio_consumable})

def building_consumable(request):
    # 1st solution
    build_consumable = Consumable.objects.filter(
        department='4')
    # This command will retrieve indians nationality peoples
    return render(request, 'myapp/build_consumable.html',
                  {'build_consumable': build_consumable})


def mechanical_activities(request):
    # 1st solution
    mech_todo = Requisition.objects.filter(
        section='1').order_by('-date')
    ac_todo=Requisition.objects.filter(sub_unit='air_conditioner')
    plumb_todo=Requisition.objects.filter(sub_unit='plumbing')
    gen_todo=Requisition.objects.filter(sub_unit='generator')
          
          
    return render(request, 'myapp/mech_activities.html',
                  {'mech_todo': mech_todo, 'ac_todo':ac_todo,'plumb_todo':plumb_todo, 'gen_todo':gen_todo})

def electrical_activities(request):
    
    elect_todo = Requisition.objects.filter(
        section='2')
    power_todo=Requisition.objects.filter(sub_unit='power')
    lv_todo=Requisition.objects.filter(sub_unit='low voltage')
    intwire_todo=Requisition.objects.filter(sub_unit='internal wiring')
    return render(request, 'myapp/elect_activities.html',
                  {'elect_todo': elect_todo,'power_todo':power_todo,'lv_todo':lv_todo,'intwire_todo':intwire_todo})

def biomedical_activities(request):
  
    bio_todo = Requisition.objects.filter(
        section='3')
    # This command will retrieve indians nationality peoples
    return render(request, 'myapp/bio_activities.html',
                  {'bio_todo': bio_todo})

def building_activities(request):
    # 1st solution
    build_todo = Requisition.objects.filter(
        department='4')
    # This command will retrieve indians nationality peoples
    return render(request, 'myapp/build_activities.html',
                  {'build_todo': build_todo})


def work_done(request):      
    work_completed=Workorder.objects.filter(completed=True)
    return render(request,"myapp/work_done.html",{
                  "work_completed":work_completed 
                  
            })
    
def sendSmS():
    url = "https://api.ng.termii.com/api/sms/send"
    payload = {
            "to": "2347032997372",
            "from": "Titus",
            "sms": "pls check the platform a request for repair was just sent to you",
            "type": "plain",
            "channel": "generic",
            "api_key": "TLzUzCFl7Q7HCJV1GWULHevnI8uP2iwFayb1UhsLGM3ODWt4BmRFiEzRo13ZmY",
                #  "media": {
                #     "url": "https://media.example.com/file",
                #     "caption": "your media file"
                # }   
        }
    headers = {
    'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text)      
    

# class WorkDoneListView(ListView):
#     model=Workorder
#     template_name="myapp/work_done.html"
      
   
# class WorkItemListView(ListView):
#     model=WorkDoneItem
#     template_name='myapp/todo_list.html'
    
#     def get_queryset(self):
#          return WorkDoneItem.objects.filter(work_list_id=self.kwargs["work_id"])
     
#     def get_context_data(self):
#         context = super().get_context_data()
#         context["work_list"] = TodoList.objects.get(id=self.kwargs['work_id'])
#         return context
# class WorkCreate(CreateView):
#     model=TodoList
#     fields=['title']
    
#     def get_context_data(self):
#         context = super(ListCreate, self).get_context_data()
#         context["title"] = "Add a new list"
#         return context
    
#     # def get_context_data(self):
#     #      context = super().get_context_data()
#     #      context["todo_list"] = TodoList.objects.get(id=self.kwargs['list_id'])
#     #      return context
# class ItemCreate(CreateView):
#     model=TodoItem
#     fields=[
#         'todo_list',
#         'title',
#         'description',
#         'due_date',
        
#             ]
#     def get_initial(self):
#         initial_data=super(ItemCreate, self).get_initial()
#         todo_list=TodoList.objects.get(id=self.kwargs['list_id'])
#         initial_data['todo_list']=todo_list
#         return initial_data
    
#     def get_context_data(self):
#         context=super(ItemCreate, self).get_context_data()
#         todo_list= TodoList.objects.get(id=self.kwargs['list_id'])
#         context['todo_list']=todo_list
#         context['title']= 'Create a new item'
#         return context
         
#     def get_success_url(self):
#         return reverse("list", args=[self.object.todo_list_id])
    
# class ItemUpdate(UpdateView):
#     model=TodoItem
#     fields=['todo_list',
#             'title',
#             'description',
#             'due_date',]
    
#     def get_context_data(self):
#         context= super(ItemUpdate, self).get_context_data()
#         context['todo_list']= self.object.todo_list
#         context['title']='Edit item'
#         return context
        
#     def get_success_url(self):
#         return reverse('list', args=[self.object.todo_list_id])

# class ListDelete(DeleteView):
#     model=TodoList
#     #use reverse_lazy() instead of reverse()
#     #as the urls are not loaded when the file s imported
#     success_url=reverse_lazy('to-do')
    
# class ItemDelete(DeleteView):
#     model=TodoItem
    
#     def get_success_url(self):
#         return reverse_lazy("list", args=[self.kwargs['list_id']])  
    
#     def get_context_data(self, **kwargs):
#         context =super().get_context_data(**kwargs) 
#         context['todo_list']= self.object.todo_list 
#         return context


      
        

    


def show_workorder(request, workorder_id):
    workorder=Workorder.objects.get(pk=workorder_id)
    return render(request, 'myapp/show_workorder.html',{
          'workorder':workorder
     })
def update_equipment(request, equipment_id):
    update_equipment=Workorder.objects.get(pk=equipment_id)  
    form=EquipmentForm(request.POST or None, instance=update_equipment)
    if form.is_valid():
            form.save()
            return redirect('all-equipments')
     
    return render(request,'myapp/update_equipment.html',{
          'update_equipment':update_equipment, 'form':form
     })

def update_asset(request, asset_id):
    update_asset=Asset.objects.get(pk=asset_id)  
    form=AssetForm(request.POST or None, instance=update_asset)
    if form.is_valid():
            form.save()
            return redirect('all-asset')
     
    return render(request,'myapp/update_asset.html',{
          'update_asset':update_asset, 'form':form
     })


def update_workorder(request, workorder_id):
    update_workorder=Workorder.objects.get(pk=workorder_id)  
    form=WorkorderForm(request.POST or None, instance=update_workorder)
    if form.is_valid():
            form.save()
            return redirect('all-workorder')
     
    return render(request,'myapp/update_workorder.html',{
          'update_workorder':update_workorder, 'form':form
     })
def update_activities(request, activity_id):
    update_activity=Requisition.objects.get(pk=activity_id)  
    form=RequisitionForm(request.POST or None, instance=update_activity)
    if form.is_valid():
            form.save()
            return redirect('all-activities')
     
    return render(request,'myapp/update_workorder.html',{
          'update_activity':update_activity, 'form':form
     })
def search_workorder(request):
    if request.method=="POST":
        searched=request.POST['searched']
        workorders=Workorder.objects.filter(requesting_unit__contains=searched)
        return render(request,"myapp/search_workorder.html",{
                  "searched":searched, "workorders":workorders
            })
      
    else: 
        return render(request,"myapp/search_workorder.html",{})
      
def all_vendors(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    vendor_list = Vendor.objects.all()
     
    p=Paginator(Vendor.objects.all(), 4)
    page=request.GET.get('page')
    vendors=p.get_page(page)
    nums="a"*vendors.paginator.num_pages

    return render(request,'myapp/vendor_list.html', {
            "vendor_list":vendor_list, 'vendors':vendors, "nums":nums
      })    

def all_workorders(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    workorder_list = Workorder.objects.all()
     
    p=Paginator(Workorder.objects.all(), 4)
    page=request.GET.get('page')
    workorders=p.get_page(page)
    nums="a"*workorders.paginator.num_pages

    return render(request,'myapp/workorder_list.html', {
            "workorder_list":workorder_list, 'workorders':workorders, "nums":nums
      })    
def all_requests(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    requisitions = Requisition.objects.all()
     
    p=Paginator(Requisition.objects.all(), 4)
    page=request.GET.get('page')
    requests=p.get_page(page)
    nums="a"*requests.paginator.num_pages

    return render(request,'myapp/request_list.html', {
            "requisitions":requisitions, 'requests':requests, "nums":nums
      })       
 
def all_assets(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    assets = Asset.objects.all()
     
    p=Paginator(Asset.objects.all(), 4)
    page=request.GET.get('page')
    assets=p.get_page(page)
    nums="a"*assets.paginator.num_pages

    return render(request,'myapp/asset_list.html', {
             'assets':assets, "nums":nums
      })       
def all_equipments(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    equipments = Equipment.objects.all()
     
    p=Paginator(Equipment.objects.all(), 4)
    page=request.GET.get('page')
    equipments=p.get_page(page)
    nums="a"*equipments.paginator.num_pages

    return render(request,'myapp/equipment_list.html', {
             'equipments':equipments, "nums":nums
      })       
          

def calendar1(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
     
                  
                month=month.capitalize()
                month_number=list(calendar.month_name).index(month)
                month_number=int(month_number)

                cal=HTMLCalendar().formatmonth(year,month_number)
                now=datetime.now()
                current_year=now.year
                time=now.strftime('%I:%M:%S:%p')
                
                workorder_list=Workorder.objects.filter(
                      date_received__year=year,
                      date_received__month=month_number
                )

                                       
                return render(request, "myapp/calendar.html", {
        
               "year":year,
               "time":time,
               "month":month,
               "month_number":month_number,
               "cal":cal,
               "current_year":current_year,
               "workorder_list":workorder_list
        
             
        
     
    })
def signup(request):
     if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            form.save()
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, ('registration successful'))
                return redirect('home')
     else:
        form=SignUpForm()

     return render(request, 'authentication/signup.html',{
            'form':form,})

    
def equipment(request):
    equipment=Equipment.objects.all().order_by('-last_service')
    return render(request,"myapp/prev_maint.html", {
                  "equipment":equipment})

def activities(request):
    activity=Activities.objects.all()
    return render(request,"myapp/activities", {
        "activity":activity
    })
def index(request):
    return render(request, "myapp/index.html")
     
# def send_emails(request):  
#     if request.method == "POST": 
#         with get_connection(  
#               host=settings.EMAIL_HOST, 
#         port=settings.EMAIL_PORT,  
#        username=settings.EMAIL_HOST_USER,  
#        password=settings.EMAIL_HOST_PASSWORD,  
#         use_tls=settings.EMAIL_USE_TLS 
#         ) as connection:  
#             recipient_list = request.POST.get("email").split()  
#             subject = request.POST.get("subject")  
#             email_from = settings.EMAIL_HOST_USER  
#             message = request.POST.get("message")  
#             print(type(recipient_list)) 
#             EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
  
    #return render(request, 'send_emails.html')

def email_add(request):
    if request.method=="POST":
        message=request.POST.get('message',False)
        email=request.POST.get('email',False)
        name=request.POST.get('name',False)
        send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False)
        return render(request, 'myapp/email.html',{
            'name':name
        })
    else:
        return render (request,'myapp/email.html', {})
                
