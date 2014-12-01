from django.conf.urls import patterns, include, url

from django.contrib import admin

from .import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_pupkin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    	
    url(r'^$', views.standard),
	url(r'^login/$',views.login),
	url(r'^signup/$',views.signup)
	)

