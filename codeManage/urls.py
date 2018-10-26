from django.conf.urls import url
from codeManage import views
urlpatterns=[
    url(r'^majorCode/$',views.majorCode),#专业代码维护
    url(r'^gradeCode/$',views.gradeCode),#年级代码维护
    url(r'^classCode/$',views.classCode),#班级代码维护
    url(r'^subjectCode/$',views.subjectCode),#学科代码维护
]