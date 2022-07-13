from rest_framework import serializers
from Api.models import Authentication




class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication
        fields = ("key",)

    
    def Validation(self, validated_data):
        try:
            Key = Authentication.objects.filter(key=int(validated_data["key"])).values("key")[0]["key"]
            return Key
        except:
            return None
        