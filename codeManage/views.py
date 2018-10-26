from django.shortcuts import render

# Create your views here.
def majorCode(request):
    return render(request,'majorCode.html')


def gradeCode(request):
    return render(request,'gradeCode.html')



def classCode(request):
    return render(request,'classCode.html')


def subjectCode(request):
    return render(request,'subjectCode.html')