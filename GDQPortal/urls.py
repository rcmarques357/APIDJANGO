from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'process',views.ProcessInformationViewSet,basename="process")

urlpatterns = [
    #path('',views.index,name="landing"),
    path('',include(router.urls)),
]