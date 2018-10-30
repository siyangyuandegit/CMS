from django.http import HttpResponse, response
from django.shortcuts import render
from django.contrib import messages
from django.template import Template, Context
# Create your views here.
def stuInfo(request):
    if request.method == 'GET':
        return render(request,'stuInfo.html')
    else:
        from index.models import Stuinfo,Admissionsforms
        cls = request.POST.get('sclass',0)
        age = request.POST.get('sage',0)
        sid = request.POST.get('sid',0)
        sname = request.POST.get('sname',0)
        gender = request.POST.get('gender',0)
        sidnum = request.POST.get('sidnum',0)
        sbirthdate = request.POST.get('sbirthdate',0)
        saddress = request.POST.get('saddress',0)
        sphone = request.POST.get('sphone',0)
        politicstatus = request.POST.get('sstatus',0)
        health = request.POST.get('shealth',0)
        # print(cls)
        stu = Stuinfo()
        stu.sid=Admissionsforms.objects.get(sid=sid)
        stu.identitynum=sidnum
        stu.gender=gender
        stu.birthdate=sbirthdate
        stu.address=saddress
        stu.age=age
        stu.tel=sphone
        stu.politicstatus=politicstatus
        stu.health=health
        stu.save()
        return render(request,'stuInfo.html')


def stuCheckIn(request):
    if request.method =='GET':
        return render(request,'stuCheckIn.html')
    else:
        sid = request.POST.get('sid','007')#学生编号
        sname = request.POST.get('sname','007')#学生姓名
        cname = request.POST.get('cname','007')#班级名称
        mname = request.POST.get('mname','007')#专业名称
        indate = request.POST.get('indate','007')#入学日期
        agent = request.POST.get('agent','007')#经办人
        inscore = request.POST.get('inscore','007')#入学分数
        from index.models import Admissionsforms,Clazz,Grade,Major
        try:
            Major.objects.get(mname=mname)
        except:
            Major.objects.create(mname=mname)#创建专业
        gdate = int(indate[:4])
        try:
            Grade.objects.get(gid=gdate)
        except:
            Grade.objects.create(**{'gid':gdate,'gname':'%s'%(str(gdate)+'级')})#创建年级
        try:
            grade = Grade.objects.get(gid=gdate)
            major = Major.objects.create(mname=mname)
            Clazz.objects.get(cname=str(grade.gid)+str(major.mid)+cname)
        except:
            cls = Clazz()
            major = Major.objects.create(mname=mname)
            grade = Grade.objects.get(gid=gdate)
            cls.cname = str(grade.gid)+str(major.mid)+cname
            cls.gid = Grade.objects.get(gid=gdate)
            cls.mid = Major.objects.get(mname=mname)
            cls.save()  # 创建班级
        try:
            Admissionsforms.objects.get(sid = sid)
        except:
            grade = Grade.objects.get(gid=gdate)
            major = Major.objects.create(mname=mname)
            cls = Clazz.objects.get(cname=str(grade.gid)+cname)
            ad = Admissionsforms()
            ad.sid=indate[2:4]+str(major.mid)+str(cls.cid)+sid
            ad.cname=cls
            ad.sname=sname
            ad.indate=indate
            ad.inscore=inscore
            ad.agent=agent
            ad.save()
        messages.success(request, '添加成功')
        return render(request,'stuCheckIn.html')
    messages.error(request, '添加失败')
    return render(request,'stuCheckIn.html')


def stuInfoMaintain(request):

    if request.method =='GET':
        return render(request, 'stuInfoMaintain.html')
    else:
        from index.models import Admissionsforms,Stuinfo
        condition = request.POST.get('condition','')
        qcondition=request.POST.get('qconditon','')
        stu = 0
        ad = 0
        if qcondition=='sid':
            stu = Stuinfo.objects.get(sid=condition)
        elif qcondition=='sname':
            ad = Admissionsforms.objects.filter(sname=condition)
            print(ad)
            stu = []
            for ad in ad:
                stu.append(Stuinfo.objects.get(sid=ad.sid))
                print(stu)
        elif qcondition=='identityNum':
            stu = Stuinfo.objects.get(identitynum=condition)
        try:
            iter(stu)
        except:
            stu = [stu,'']
        return render(request, 'stuInfoMaintain.html', {'stu': stu})



def stuRegQuery(request):
    if request.method =='GET':
        return render(request, 'stuRegQuery.html')
    else:
        from index.models import Admissionsforms,Stuinfo
        condition = request.POST.get('condition','')
        qcondition=request.POST.get('qconditon','')
        oc = request.POST.get('oc','')
        stu = []
        if qcondition=='sid':
            if oc=='__gt':
                # q = qcondition+'__sid'+oc
                # print(q)
                stu = Stuinfo.objects.filter(sid__sid__gt=condition)
            elif oc == '__lt':
                stu = Stuinfo.objects.filter(sid__sid__lt=condition)
            elif oc == '==':
                stu = Stuinfo.objects.get(sid__sid__exact=condition)
            elif oc == '__gte':
                stu = Stuinfo.objects.filter(sid__sid__gte=condition)
            elif oc == '__lte':
                stu = Stuinfo.objects.filter(sid__sid__lte=condition)
            try:
                iter(stu)
            except:
                stu = ['',stu]
        elif qcondition=='indate':
            def sizeOfDate(oc):
                from django.db import connection
                cursor = connection.cursor()
                # print("SELECT * from admissionsforms where DATE_FORMAT(indate,'%Y%m%d') >"+condition)
                cursor.execute("SELECT * from admissionsforms where DATE_FORMAT(indate,'%Y%m%d')"+oc + condition)
                a = cursor.fetchall()
                for a in a:
                    stu.append(Stuinfo.objects.get(sid=a[0]))
            if oc == '__gt':
                sizeOfDate('>')
            elif oc == '__lt':
                sizeOfDate('<')
            elif oc == '==':
                sizeOfDate('=')
            elif oc == '__gte':
                sizeOfDate('>=')
            elif oc == '__lte':
                sizeOfDate('<=')
        elif qcondition=='inscore':
            condition=str('%.2f'%float(condition))#如果先转整形会出现输入小数无法转换为整数
            def sizeOfIndate(oc):
                from django.db import connection
                cursor = connection.cursor()
                # print("SELECT * from admissionsforms where DATE_FORMAT(indate,'%Y%m%d') >"+condition)
                cursor.execute("SELECT * from admissionsforms where inscore"+oc + condition)
                a = cursor.fetchall()
                for a in a:
                    stu.append(Stuinfo.objects.get(sid=a[0]))
            if oc == '__gt':
                sizeOfIndate('>')
            elif oc == '__lt':
                sizeOfIndate('<')
            elif oc == '==':
                sizeOfIndate('=')
            elif oc == '__gte':
                sizeOfIndate('>=')
            elif oc == '__lte':
                sizeOfIndate('<=')
        return render(request, 'stuRegQuery.html', {'stu': stu})



def teachInfo(request):
    return render(request,'teachInfo.html')



def teachInfoMt(request):
    return render(request,'teachInfoMt.html')