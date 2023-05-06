from .views import CategoryViewset, ProductViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("categorys/", CategoryViewset)
router.register("prducts/", ProductViewset)

urlpatterns = [

]