from django.shortcuts import render

# Create your views here.
def userAdd(request):
    return render(request,'userAdd.html')

def userQuery(request):
    return render(request,'userQuery.html')