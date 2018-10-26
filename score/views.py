from django.shortcuts import render

# Create your views here.
def record(request):
    return render(request,'record.html')


def query(request):
    return render(request,'query.html')



def classScore(request):
    return render(request,'classScore.html')


def gradeScore(request):
    return render(request,'gradeScore.html')
