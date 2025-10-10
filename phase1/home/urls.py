from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = " LOKESH SITE"
admin.site.site_title = " LOKESH RULE SITE PORTAL"
admin.site.index_title = "Welcoem to lokesh website portal"

urlpatterns = [
    path("", views.index, name= "home"),
    path("about",views.about, name = "about" ),
    path("services" , views.services, name = "services"),
    path("contact" , views.contact, name = "contact")
]
