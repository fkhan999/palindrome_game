from rest_framework import serializers
from .models import *

class palindromeSerializers(serializers.ModelSerializer):
    class Meta:
        model=palindrome
        fields='__all__'