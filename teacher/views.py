# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from index.models import *


def teaching(request):
    if request.method == 'GET':
        return render(request, 'teaching.html')
    else:
        tidd = request.POST.get('tid')
        # print(tidd)
        # print(type(tidd))
        # tid = int(tid)
        if tidd:
            tinfo = Teacherinfo.objects.filter(tid=tidd)
            return render(request, 'teaching.html', {'tinfo': tinfo})
        return render(request, 'teaching.html')


def teachQuery(request):
    if request.method == 'GET':
        return render(request, 'teachQuery.html')
    else:
        cid = request.POST.get('sel', '')
        both = request.POST.get('all', '')
        print(cid,both)
        if cid == 'curid':
            login = Course.objects.filter(curname=both)
            print(login)
            tlist = []
            for i in login:
                curid = i.curid
                # print(curid)
                tid = Techcourse.objects.filter(curid__curid=curid)
                for j in tid:
                    teachid = j.tid
                    tlist.append(teachid)
            return render(request, 'teachQuery.html', {'teachid': tlist, 'login':login})

        elif cid == 'tname':
            ttid = Teacherinfo.objects.filter(tname=both)
            # print(ttid)
            list = []
            for k in ttid:
                # print(k)
                tid = k.tid
                print(tid)
                teachcourse = Techcourse.objects.filter(tid__tid=tid)
                # print(teachcourse)
                for l in teachcourse:
                    # print(l)
                    cuorseid = l.curid
                    a=cuorseid.curname
                    # print(a)
                    list.append(cuorseid)

        return render(request, 'teachQuery.html', {'teachid': ttid, 'login': list})

def teachQuery1(request,num):
        b = Techcourse.objects.filter(tid=num)
        for j in b:
            cur = j.curid.curid

        a = Teacherinfo.objects.filter(tid=num)
        for i in a:
            cid = i.mid.mid
            # print(cid)
        Techcourse.objects.get(tid=num).delete()
        # Major.objects.get(mid=cid).delete()
        Teacherinfo.objects.get(tid=num).delete()


        Course.objects.get(curid=cur).delete()



        return render(request, 'teachQuery.html')
