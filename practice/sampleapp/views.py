from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.


def student_data(request):

    #std_data = Student.objects.all()   # select * from sampleapp_student
    std_data = Student.objects.filter(age__gt=10)
    return render(request, 'student_data.html', {'std_data': std_data})


    #return HttpResponse(std_data)


