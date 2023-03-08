from rest_framework import serializers
from .models import Guideline


class GuidelineSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=250)
    version = serializers.CharField(max_length=10)
    text = serializers.CharField()
    created_date = serializers.DateTimeField()
    publish_date = serializers.DateTimeField()
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url='images/')

    class Meta:
        model = Guideline
        fields = ('__all__')
