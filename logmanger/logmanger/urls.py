from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'logmanger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^check/','logmangerapp.views.view',name='view'),
    url(r'^check2/','logmangerapp.views.view2',name='view2')
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

