from rest_framework.serializers import ModelSerializer
from .models import Students


class StudentsSerializer(ModelSerializer):
      class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'age', 'gender')