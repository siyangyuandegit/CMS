from django.http import HttpResponse
from django.shortcuts import render
from index.models import *

# Create your views here.
def bookInfo(request):
    return render(request,'bookInfo.html')


def bookMaintain(request):
    if request.method =='GET':
        return render(request,'bookMaintain.html')
    else:
        re = request.POST.get('select')
        if re =='bookid':
            id = request.POST.get('info')
            id=int(id)
            try :
                 all = Bookinfo.objects.get(bid=id)
                 return render(request,'bookMaintain.html',{'all':all})
            except:
                return HttpResponse('没有这本书')
        else:
            name = request.POST.get('info')
            try :
                all = Bookinfo.objects.get(bname=name)
                return render(request, 'bookMaintain.html', {'all': all})
            except:
                return HttpResponse('没有这本书')



def bookBorrow(request):
    return render(request,'bookBorrow.html')


def bookReturn(request):
    return render(request,'bookReturn.html')


def borrowQuery(request):
    return render(request,'borrowQuery.html')


def bookupdate(request,num):
    if request.method =='GET':
        all = Bookinfo.objects.get(bid=num)
        return render(request,'bookupdate.html',{'all':all})
    else:
        bookid = request.POST.get('bookid')
        bookname = request.POST.get('bookname')
        bpub = request.POST.get('bookp')
        bprice = request.POST.get('bookprice')
        bn = request.POST.get('booknum')
        try:
            Bookinfo.objects.filter(bid=num).update(bid=bookid,bname=bookname,publication=bpub,price=bprice,bnum=bn)
            return HttpResponse('更改成功')
        except:
            return HttpResponse('输入有误')
