"""
URL configuration for farmer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from farmerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',views.index),
    path('farmerregister/',views.farmerregister),
    path('farmtechregister/',views.farmtechregister),
    path('login/',views.login),
    path('farmer/',views.farmer),
    path('farmtech/',views.farmtech),
    path('admin1/',views.admin1),
    path('logout/',views.logout),
    path('addproducts/',views.addproducts),
    path('applyloan/',views.applyloan),
    path('addcategory/',views.addcategory),
    path('viewcategory/',views.viewcategory),
    path('deleteproducts/',views.deleteproducts),
    path('viewproducts/',views.viewproducts),
    path('deletecategory/',views.deletecategory),
    path('updateproducts/',views.updateproducts),
    path('farmtechviewcategory/',views.farmtechviewcategory),
    path('farmtechviewproducts/',views.farmtechviewproducts),
    path('actionproducts/',views.actionproducts),
    path('adminviewfarmer/',views.adminviewfarmer),
    path('adminviewfarmtech/',views.adminviewfarmtech),
    path('admindeletefarmer/',views.admindeletefarmer),
    path('admindeletefarmtech/',views.admindeletefarmtech),
    path('feedback/',views.feedback),
    path('admin_feedback/',views.admin_feedback),
    path('farmerviewfarmtech/',views.farmerviewfarmtech),
    path('farmtechviewloan/',views.farmtechviewloan),
    path('addrent/',views.addrent),
    path('addvehicle/',views.addvehicle),
    path('addland/',views.addland),
    path('viewvehiclerent/',views.viewvehiclerent),
    # path('deleteactions/',views.deleteactions),
    path('actionloans/',views.actionloans),
    path('deleteloans/',views.deleteloans),
    path('deletevehicle/',views.deletevehicle),
    path('updatevehicle/',views.updatevehicle),
    path('viewlandrent/',views.viewlandrent),
    path('updateland/',views.updateland),
    path('rent/',views.rent),
    path('farmerviewvehicle/',views.farmerviewvehicle),
    path('bookrent/',views.bookrent),
    path('farmerviewland/',views.farmerviewland),
    # path('actionvehicle/',views.actionvehicle),
    path('booklandrent/',views.booklandrent),
    path('bookedrent/',views.bookedrent),
    path('delete/',views.delete),
    path('vehiclepayment/',views.vehiclepayment),
    path('landpayment/',views.landpayment),
    path('deleteland/',views.deleteland),
   
    
]
