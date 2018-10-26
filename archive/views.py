from django.shortcuts import render

# Create your views here.
def stuInfo(request):
    return render(request,'stuInfo.html')


def stuCheckIn(request):
    return render(request,'stuCheckIn.html')



def stuInfoMaintain(request):
    return render(request,'stuInfoMaintain.html')



def stuRegQuery(request):
    return render(request,'stuRegQuery.html')



def teachInfo(request):
    return render(request,'teachInfo.html')



def teachInfoMt(request):
    return render(request,'teachInfoMt.html')