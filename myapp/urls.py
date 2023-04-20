from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backgroundimages', views.background),
    path('', views.images),
    path('imagetext', views.imagetext),
    path('form', views.form),
]
