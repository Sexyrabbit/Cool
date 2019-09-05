from .api import IncidentViewSet, ConfigItemViewSet, ApplicationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cis',ConfigItemViewSet)
router.register(r'incs',IncidentViewSet)
router.register(r'apps',ApplicationViewSet)

urlpatterns = router.urls