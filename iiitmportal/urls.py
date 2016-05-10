from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from iiitm import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'iiitm.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^iiitm/', include('iiitm.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^profile/$', 'registration.views.profile', name='profile'),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'^media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT}),
		)