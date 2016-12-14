from django.conf.urls import url
from . import views


urlpatterns = [ 
    
    #Tasks
    url('^tasks/$', views.Task_List_Create.as_view(), name='tasks'),
    url('^task/(?P<pk>[0-9]+)/$', views.Task_Detail.as_view(), name='task-detail'),

] 