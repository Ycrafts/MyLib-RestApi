from django.urls import path
from .views import BookViewSet, CategoryViewSet, AuthorViewset, FavoriteViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("books", BookViewSet, basename="books")
router.register("categorys", CategoryViewSet, basename="categorys")
router.register("authors", AuthorViewset, basename="authors")
router.register("favorites", FavoriteViewSet, basename="favorites")


urlpatterns = router.urls

