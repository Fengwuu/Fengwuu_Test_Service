from django.conf.urls.static import static
from django.urls import path, include
from fengwuu_test import settings

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
