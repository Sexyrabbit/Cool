from .api import STViewSet, CIViewSet, APPViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
router = DefaultRouter()
router.register(r'supportteam',STViewSet)
router.register(r'configitem',CIViewSet)
router.register(r'application',APPViewSet)


#urlpatterns = [
#    path('supportteam', include(router.urls)),
#    path('configitem', CISerializer.as_view(), name="configitem"),
#]

urlpatterns = router.urls