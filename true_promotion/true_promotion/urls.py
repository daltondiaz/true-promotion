from django.conf.urls import url, include
from django.contrib import admin
from api import views
from rest_framework.routers import DefaultRouter


# Create a router and register views with it.
router = DefaultRouter()
router.register(r'products',views.ProductViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, include the login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
