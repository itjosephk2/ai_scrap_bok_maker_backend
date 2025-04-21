from rest_framework import serializers
from .models import ScrapImage


class ScrapImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapImage
        fields = '__all__'
        read_only_fields = ['edited_image', 'caption']
