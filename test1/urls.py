from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^$", 'sigegov.views.main'),
    url(r'^sigegov/', include('sigegov.urls')),
    url(r'^chat/', include('djangoChat.urls')),
    url(r'', include('social_auth.urls')),
    url(r'', include('django.contrib.auth.urls')),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
