from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('room', views.RoomViewSet)
router.register('lecturer', views.LecturerViewSet)
router.register('student', views.StudentViewSet)
router.register('schedule', views.ScheduleViewSet)
router.register('jadwal',views.JadwalViewSet)
router.register('kuliah',views.KuliahViewSet)
# router.register('auditresult/(?P<pk>[0-9]+)/$',views.AuditResultDetail)


urlpatterns = [
    url(r'', include(router.urls)),
]
