from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ProcessInformation
from .serializers import ProcessInformationSerializer

class ProcessInformationViewSet(viewsets.ModelViewSet):
    queryset=ProcessInformation.objects.all().order_by('-process_number')
    serializer_class=ProcessInformationSerializer

    @action (detail=False, methods=['get'])
    def stats(self,request):
        return Response({'total': ProcessInformation.objects.count(),
                        'Completed': ProcessInformation.objects.filter(process_status='completed').count(),
                        'In Progress': ProcessInformation.objects.filter(process_status='inprogress').count()
                        })

#def index(request):
#    return render(request,'GDQPortal/landing.html')