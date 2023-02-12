from django.shortcuts import render
from.models import Student
from .serializers import StudentSerialization
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.

def student_detail(request):
    stu=Student.objects.get(id=1)
    serializer=StudentSerialization(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
