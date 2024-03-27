from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from shop.views import CategoryViewset, ProductViewset

route = SimpleRouter()
route.register("category", CategoryViewset, basename="category")
route.register("product", ProductViewset, basename="product")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include(route.urls))
]
