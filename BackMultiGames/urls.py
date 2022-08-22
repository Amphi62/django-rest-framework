from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from solitaire.views import SolitaireViews

router = routers.DefaultRouter()
router.register(r'solitaire', SolitaireViews)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
