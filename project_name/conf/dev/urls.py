from django.conf.urls import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


CONF_MODULE = '%s.conf' % settings.PROJECT_NAME

urlpatterns = patterns(
    '',
    (r'', include('%s.urls' % CONF_MODULE)),
)
urlpatterns += staticfiles_urlpatterns()
