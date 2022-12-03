from django.urls import path, include
from hints_drf.views import TestViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'answers', TestViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls),  ),

]
