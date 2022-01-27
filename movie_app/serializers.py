from rest_framework import serializers 

class SearchSerializer(serializers.Serializer):
  title = serializers.CharField(max_length=255,allow_blank=True,allow_null=True)
  overview = serializers.CharField(max_length=255,allow_blank=True,allow_null=True)
  date = serializers.DateField(allow_null=True)