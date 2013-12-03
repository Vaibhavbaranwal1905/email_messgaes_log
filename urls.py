from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('email_messages_log.views',
	url(r'^', 'email_messages_listing', name='email_messages_listing'),

)