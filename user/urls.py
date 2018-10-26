from django.conf.urls import url
from user import views
urlpatterns=[
    url(r'^userAdd/$',views.userAdd),#用户添加
    url(r'^userQuery/$',views.userQuery),#用户查询
]