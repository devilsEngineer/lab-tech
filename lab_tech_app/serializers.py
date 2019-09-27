from rest_framework_mongoengine import serializers
from lab_tech_app.models import Patient

class PatientSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Patient
        fields = '__all__'