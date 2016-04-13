"""imagersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import home_page, ClassView
from django.views.generic import TemplateView

urlpatterns = [
    # regex ^ means line MUST start with whatever follows. e.g. 'admin/'
    # regex $ means end of the line.  if this character is not present, view will match from on.  if present, will only match until this
    url(r'^admin/', admin.site.urls),
    # url(r'^profile/', imager_profile.urls),
    # url(r'^$', home_page, name='home_page'),
    # url(r'^home/(?P<id>[0-9])$', home_page, name='home_page')
    # url(r'^home/([0-9])$', home_page, name='home_page')  # this line returns an arg (unnamed) of the pattern.  previous line returns a kwarg (named)
    # url(r'^home/(?P<id>[0-9])$', ClassView.as_view(), name='home_page')
    url(r'^home/(?P<id>[0-9])$', TemplateView.as_view(template_name='home.html'), name='home_page')
]


# can create sublists which are joined into urlpatterns
'''
image_urls = []
profile_urls = []
api_urls = []
urlpatterns = image_urls + profile_urls + api_urls
'''


# THIS IS FOR DEV.  IN PRODUCTION AN ACTUAL SERVER WILL EXIST.  (also, turn off debug in settings.py)
# if settings.DEBUG:
#     urlpatterns += (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
