from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls.views import hello, contact, student, best

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', hello),
	url(r'^contact/$', contact),
	url(r'^student_list/$', student),
	url(r'^student_detail/$', best),
)
