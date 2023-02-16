from django.shortcuts import render
from quickstart.models import Students
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework import generics
from .serializer import StudentsSerializer

# Create your views here.

# class StudentView(APIView):
#     def get(self, request):
#         lst = Students.objects.all().values()
#         return Response({'students':list(lst)})

#     def post(self, request):
#         post_new = Students.objects.create(
#             first_name = request.data['first_name'],
#             last_name = request.data['last_name'],
#             age = request.data['age'],
#             gender = request.data['gender']
#         )
#         return Response({'post':model_to_dict(post_new)})


class StudentListView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentDestroyView(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)