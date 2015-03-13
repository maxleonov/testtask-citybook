from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from citybook import views


router = DefaultRouter()
router.register(r'city', views.CityViewSet, 'city')

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='home.html')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api/', include(router.urls)),
)

