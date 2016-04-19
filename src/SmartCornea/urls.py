from django.conf.urls import patterns, include, url
from django.contrib import admin
import face_detector.views 
 
urlpatterns = patterns('',
                       # Examples:
 
    url(r'^face_detector/detect/$', 'face_detector.views.detect'),
 
    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include(admin.site.urls)),
)