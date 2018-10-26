from django.shortcuts import render

# Create your views here.
def teaching(request):
    return render(request,'teaching.html')


def teachQuery(request):
    return render(request,'teachQuery.html')
