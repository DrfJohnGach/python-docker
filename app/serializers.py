from rest_framework import serializers

from .models import Student

# Student serializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','username', 'course')
