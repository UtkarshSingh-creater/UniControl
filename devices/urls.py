from django.urls import path

from . import views

urlpatterns = [

    path("",views.device_list,name="device_list",),

    path("add/",views.device_create,name="device_create",),

    path("<int:pk>/edit/",views.device_update,name="device_update",),

    path("<int:pk>/delete/",views.device_delete,name="device_delete",),
    
    path("pair/<int:pk>/",views.pair_device,name="pair_device",),

]