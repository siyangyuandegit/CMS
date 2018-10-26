from django.shortcuts import render

# Create your views here.
def bookInfo(request):
    return render(request,'bookInfo.html')


def bookMaintain(request):
    return render(request,'bookMaintain.html')


def bookBorrow(request):
    return render(request,'bookBorrow.html')


def bookReturn(request):
    return render(request,'bookReturn.html')


def borrowQuery(request):
    return render(request,'borrowQuery.html')