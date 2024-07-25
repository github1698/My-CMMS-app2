
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    #path('',views.signup,name='signup'),
    path('calendar',views.calendar1,name='calendar1'),
   # path('<int:year><str:month>/',views.index,name='home'),
    path('add_equipment',views.add_equipment,name='add-equipment'),
    path('update_equipment',views.update_equipment,name='update-equipment'),
    path('delete_equipment',views.delete_equipment, name='delete-equipment'),
    path('all_vendor',views.all_vendors,name='all-vendor'),
    path('all_workorder',views.all_workorders,name='all-workorder'),
    path('all_asset',views.all_assets,name='all-asset'),
    path('all_equipments',views.all_equipments,name='all-equipments'),
    path('all_requests',views.all_requests,name='all-requests'),
    path('add_consumable',views.add_consumable,name='add-consumable'),
    path('add_equipment',views.add_equipment,name='add-equipment'),
    path('add_workorder',views.add_workorder,name='add-workorder'),
    path('add_request',views.add_request,name='add-request'),
    path('add_asset',views.add_asset,name='add-asset'),
    path('work_order',views.work_done,name='work-order'),
   # path('equipment_list',views.index,name='equipment-list'),
    path('consumable_list',views.Consumables,name='consumable-list'),
    path('update_equipment/<equipment_id>',views.update_equipment,name='update-equipment'),
    path('update_request/<requisition_id>',views.update_request,name='update-request'),
    path('update_workorder/<workorder_id>',views.update_workorder,name='update-workorder'),
    #path('delete_activities/<activity_id>',views.delete_activities,name='delete-activities'),
    path('delete_workorder/<workorder_id>',views.delete_workorder,name='delete-workorder'),
    path('equipt', views.equipment, name='equip'),
    path('show_consumable/<consumable_id>',views.show_consumable,name='show-consumable'),
    path('show_equipment/<equipment_id>',views.show_equipment,name='show-equipment'),
    path('show_workorder/<workorder_id>',views.show_workorder,name='show-workorder'),
    path('show_asset/<asset_id>',views.show_asset,name='show-asset'),
    path('show_request/<requisition_id>',views.show_request,name='show-request'),
    path('show_vendor/<vendor_id>',views.show_vendor,name='show-vendor'),
    path('add_vendor',views.add_vendor,name="add-vendor"),
    path('list_request',views.list_request,name='list-request'),
    path('aset_list',views.asset_list,name='asset-list'),
    path('list_equipment',views.list_equipment,name='list-equipment'),
    path('list_vendor',views.list_vendor,name='list-vendor'),
    path('update_consumable/<consumable_id>',views.update_consumable,name='update-consumable'),
    path('mechanical_consumable',views.mechanical_consumable,name='mechanical-consumable'),
    path('electrical_consumable',views.electrical_consumable,name='electrical-consumable'),
    path('biomedical_consumable',views.biomedical_consumable,name='biomedical-consumable'),
    path('building_consumable',views.building_consumable,name='building-consumable'),
    path('mechanical_activities',views.mechanical_activities,name='mechanical-activities'),
    path('electrical_activities',views.electrical_activities,name='electrical-activities'),
    path('biomedical_activities',views.biomedical_activities,name='biomedical-activities'),
    path('building_activities',views.building_activities,name='building-activities'),
    path('update_vendor/<vendor_id>',views.update_vendor,name='update-vendor'),
    path('update_request/<requisition_id>',views.update_request,name='update-request'),
    path('delete_vendor/<vendor_id>',views.delete_Vendor,name='delete-vendor'),
    path('delete_request/<requisition_id>',views.delete_request,name='delete-request'),
    path('delete_consumable/<consumable_id>',views.delete_consumable,name='delete-consumable'),
    path('delete_equipment/<equipment_id>',views.delete_equipment,name='delete-equipment'),
    path('search_vendor',views.search_vendor,name='search-vendor'),
    path('search_workorder',views.search_workorder,name='search-workorder'),
    path('workorder_pdf',views.workorder_pdf,name='workorder-pdf'),
    path('workorder_csv',views.workorder_csv,name='workorder-csv'),
    path('workorder_text',views.workorder_text,name='workorder-text'),
    path('activitieslist_pdf',views.activitieslist_pdf,name='activitieslist-pdf'),
    path('workorder_csv',views.workorder_csv,name='workorder-csv'),
    path('activitieslist_csv',views.activitieslist_csv,name='activitieslist-csv'),
    path('workorder_text',views.workorder_text,name='workorder-text'),
    path('workorder_text',views.workorder_text,name='workorder-text'),
    path('activitieslist_text',views.activitieslist_text,name='activitieslist-text'),
    #path('asset_list',views.asset,name='asset-list'), 
    path('activities_list',views.Activities,name='activities-list'), 
    path('update_asset/<asset_id>',views.update_asset,name='update-asset'),
    path('delete_asset/<asset_id>',views.delete_asset,name='delete-asset'), 
    path('email_add',views.email_add,name='email-add'), 
    path('to_do',views.ListListView.as_view(),name='to-do'), 
    path('list/<int:list_id>',views.ItemListView.as_view(),name='list'), 
    path('list/add/',views.ListCreate.as_view(),name='list-add'), 
    path('list/<int:pk>/delete/',views.ListDelete.as_view(),name='list-delete'), 
    path('list/<int:list_id>/item/add',views.ItemCreate.as_view(),name='item-add'), 
    path('list/<int:list_id>/item/<int:pk>/',views.ItemUpdate.as_view(),name='item-update'),
    path('list/<int:List_id>/item/<int:pk>/delete/',views.ItemDelete.as_view(),name='item-delete'),
    
    
    
    
    
   
   
   
   
   
    
    
    
]


