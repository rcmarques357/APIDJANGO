from rest_framework import serializers
from.models import ProcessInformation, ProcessKPIInformation, ProcessKPIValue, ProcessTask


class ProcessInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProcessInformation
        fields="__all__"
        #read_only_fields=("process_number",)