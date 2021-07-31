from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        field = ('id','description','status')

    def create(self,validated_data):
        return Student.objects.create(**validated_data)