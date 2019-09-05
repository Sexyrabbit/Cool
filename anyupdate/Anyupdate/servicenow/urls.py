from .api import IncidentViewSet, ConfigItemViewSet, ApplicationViewSet, UserViewSet, GroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cis',ConfigItemViewSet)
router.register(r'incs',IncidentViewSet)
router.register(r'apps',ApplicationViewSet)


router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = router.urls