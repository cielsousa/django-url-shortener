from django.urls import path, include
from . import views
from rest_framework import routers




# API routers register
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('urls', views.UrlViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('shorted/', views.shorted, name='shorted'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', include(router.urls)),
]