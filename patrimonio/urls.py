from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, LugarViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

router.register(r'lugares', LugarViewSet)

urlpatterns = router.urls