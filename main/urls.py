from rest_framework import routers, urlpatterns
from .views import CustomerViewSet

router = routers.SimpleRouter()
router.register(r'customer',CustomerViewSet)

urlpatterns = router.urls