from django.conf.urls import url
from score import views
urlpatterns=[
    url(r'^record/$',views.record),#成绩录入
    url(r'^query/$',views.query),#成绩查询
    url(r'^classScore/$',views.classScore),#班级成绩统计
    url(r'^gradeScore/$',views.gradeScore),#年级成绩统计
]