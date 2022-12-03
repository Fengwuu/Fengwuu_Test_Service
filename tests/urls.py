from django.conf.urls.static import static
from django.urls import path
from .views import *
from fengwuu_test import settings


urlpatterns = [
    path('', home, name='home'),
    path('tests/categories/<int:category_id>/', TestsByCategory.as_view(), name='tests_by_category'),
    path('tests/test-completing/test/<int:test_id>/question/<int:question_number>/',
         user_answer,
         name='test_completing'),
    path('tests/test-completing/result/', test_result, name='result')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
