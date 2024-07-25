from django.contrib import admin
from .models import Equipment, MaintOfficers,Workorder, Vendor,Section, Asset, Consumable, Department, Requisition, Head,Activities, TodoItem,TodoList,Manager
# Register your models here.
@admin.register(MaintOfficers)
class MaintOfficersAdmin(admin.ModelAdmin):
    list_display=('first_name',"last_name")
    ordering=('first_name',)
    search_fields=('first_name',)

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display=('todo',"todo_date")
    ordering=('todo_date',)
    search_fields=('todo_date',)
       
    




@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    list_display=('emanating_dept','requesting_officer')
    ordering=('emanating_dept',)
    search_fields=('emanating_dept','requesting_office')
    

   
    
@admin.register(Workorder)
class WorkorderAdmin(admin.ModelAdmin):
    list_display=('requesting_unit','department','date_received')
    ordering=('requesting_unit',)
    search_fields=('requesting_unit','machine')
    

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display=('name','model','location')
    ordering=('location',)
    search_fields=('name','location',)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display=('name','address','phone','email_address',)
    ordering=('name',)
    search_fields=('name','phone',)

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display=('asset_name','model','asset_department','present_condition',)
    ordering=('asset_name',)
    search_fields=('asset_name','asset_department',)

@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
    list_display=('item_name','quantity','issued_to','Balance','Reorder')
    ordering=('item_name',)
    search_fields=('item_name','Reorder',)

# @admin.register(Activities)
# class ActivitiesAdmin(admin.ModelAdmin):
#     list_display=('department','work_item','date')
#     ordering=('department',)
#     search_fields=('department','date',)
    
@admin.register(Head)
class HeadAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','dept')
    ordering=('last_name',)
    search_fields=('last_name','dept')


@admin.register(Section)
class HeadAdmin(admin.ModelAdmin):
    list_display=('unit','department1')
    ordering=('department1',)
    search_fields=('unit','department1')

admin.site.register(Department)

admin.site.register(TodoItem)
admin.site.register(TodoList)
admin.site.register(Manager)



