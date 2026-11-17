from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, LugarViewSet, ResenaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

router.register(r'lugares', LugarViewSet)
router.register(r'resenas', ResenaViewSet)

urlpatterns = router.urls
