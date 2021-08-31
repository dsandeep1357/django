from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Metrics.views import index, adminlogin, adminloginentered, logout, userlogin,
userregister, viewuserdata, \
activateuser, filedata, adminpage, userlogincheck, uploadfile, viewfile, userpage,
viewfildata, userfiledata

urlpatterns = [
url(r'^admin/', admin.site.urls),
#url(r'^$', index, name="index"),
url(r'^index/', index, name="index"),
url(r'^adminpage/', adminpage, name="adminpage"),
url(r'^adminlogin/', adminlogin, name="adminlogin"),
url(r'^adminloginentered/', adminloginentered, name="adminloginentered"),
url(r'viewuserdata/', viewuserdata, name="viewuserdata"),
url(r'activateuser/', activateuser, name="activateuser"),
url(r'^filedata/', filedata, name="filedata"),
url(r'^viewfile/', viewfile, name="viewfile"),
url(r'^logout/', logout, name="logout"),

url(r'^userlogincheck/', userlogincheck, name="userlogincheck"),
url(r'^userlogin/', userlogin, name="userlogin"),
url(r'^userpage/', userpage, name="userpage"),
url(r'^userregister/', userregister, name="userregister"),
url(r'^uploadfile/', uploadfile, name="uploadfile"),
url(r'^viewfildata/', viewfildata, name="viewfildata"),
url(r'^userfiledata/', userfiledata, name="userfiledata"),
]
if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
