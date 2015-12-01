from django.conf.urls import patterns, url
#from courses.models import Course
from students import views

urlpatterns = patterns('',
    #url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
	url(r'^$', views.list_view, name='list_view'),
	url(r'^(?P<detail_id>\d+)/$', views.detail, name='detail'),
	url(r'^apply/$', views.apply_to_course, name='apply'),
  	url(r'^edit_application/(?P<pk>\d+)/$', views.edit_application, name='edit_application'),
	url(r'^delete_application/(?P<pk>\d+)/$', views.delete_application, name='delete_application'),
	url(r'^add/$', views.student_model, name='student_model'),
)
