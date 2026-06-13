from .models import About, Technology
from rest_framework import serializers

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class TechnologyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'
