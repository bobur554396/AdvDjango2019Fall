from django.urls import path
from core.views import ProjectListViewSet, ProjectViewSet
from rest_framework import routers
# from core.views import ProjectListAPIView


# urlpatterns = [
#     path('projects/', ProjectListAPIView.as_view())
# ]

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, base_name='core')

urlpatterns = router.urls

