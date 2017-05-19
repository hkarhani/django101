from django.conf.urls import url

from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # No need for base_name as model name is used
router.register('login', views.loginViewSet, base_name='login')
# order is important as once matched, it executes the class mapped to it
urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),
]
