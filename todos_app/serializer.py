from rest_framework import serializers
from todos_app.models import Task

# O serializer funciona como o filtro dos dados que eu quero disponibilizar de cada modelo.

class PublicTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'