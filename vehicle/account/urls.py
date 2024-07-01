from django.contrib import admin
from django.urls import path
from account.views import RegView,LoginView,AddVehicleView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('reg',RegView.as_view(),name="reg"),
    path('log',LoginView.as_view(),name="log"),
    path('addv',AddVehicleView.as_view(),name="addv")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

