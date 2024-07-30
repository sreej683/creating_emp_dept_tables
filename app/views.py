from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length
def equi_joins(request):
    ledo=Emp.objects.select_related('deptno').all()
    ledo=Emp.objects.select_related('deptno').filter(ename='Smith')
    ledo=Emp.objects.select_related('deptno').filter(deptno__deptno=30)
    ledo=Emp.objects.select_related('deptno').filter(deptno__dname='Research')
    ledo=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    ledo=Emp.objects.select_related('deptno').filter(ename__in=['James','Allen'])
    ledo=Emp.objects.select_related('deptno').filter(sal__lt=8000)
    ledo=Emp.objects.select_related('deptno').filter(job__startswith='R')
    ledo=Emp.objects.select_related('deptno').filter(deptno__dname__contains='e')
    ledo=Emp.objects.select_related('deptno').filter(sal__gte=2000,comm__gte=30)
    ledo=Emp.objects.select_related('deptno').filter(deptno__gte=20)
    ledo=Emp.objects.select_related('deptno').filter(Q(deptno__dname__contains='s')| Q(ename__contains='r'))
    ledo=Emp.objects.select_related('deptno').filter(Q(deptno__dname__contains='e')& Q(ename__contains='l'))
    ledo=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    ledo=Emp.objects.select_related('deptno').filter(hiredate__day=25)
    ledo=Emp.objects.select_related('deptno').filter(Q(ename__endswith='s')|Q(deptno__dname__endswith='o'))
    ledo=Emp.objects.select_related('deptno').filter(Q(ename__startswith='S')&Q(ename__endswith='h'))
    ledo=Emp.objects.select_related("deptno").filter(ename__gt=Length('ename'))
    d={'ledo':ledo}
    return render(request,'equi_joins.html',d)





def emp_dept_mgr(request):
    edm=Emp.objects.select_related('deptno','mgr').all()
    edm=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Operations')
    edm=Emp.objects.select_related('deptno','mgr').filter(ename='Smith')
    edm=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='james')
    edm=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    edm=Emp.objects.select_related('deptno','mgr').filter(sal__gt=7000)
    edm=Emp.objects.select_related('deptno','mgr').filter(comm__lte=50)
    edm=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc__in=['Chichago','Dallas'])
    edm=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__in=['Research','Sales','Operations'])
    edm=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__isnull=False)
    edm=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    edm=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname__startswith='S')| Q(ename__endswith='S'))
    edm=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname__startswith='O')& Q(deptno__dname__endswith='S'))
    edm=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__contains='S')
    edm=Emp.objects.select_related('deptno','mgr').filter(sal__lte=8000)
    edm=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='J')
    edm=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__in=['Smith','Blake'])
    edm=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    edm=Emp.objects.select_related('deptno','mgr').filter(hiredate__gt='2002-05-30')
    edm=Emp.objects.select_related('deptno','mgr').filter(hiredate__gt='2024-07-26')
    edm=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno=20)
    edm=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno=40)
    edm=Emp.objects.select_related('deptno','mgr').filter(sal__lt=6000)
    edm=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__contains='l')
    d={'edm':edm}
    return render(request,'emp_dept_mgr.html',d)