from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  EventViewSet,  AttendanceViewSet, InventoryViewSet, NoticeViewSet, GMemberViewSet, GroupViewSet
from members.views import MemberViewSet


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'inventory',InventoryViewSet)
router.register(r'notices', NoticeViewSet)
router.register(r'members', MemberViewSet, basename='members')
router.register(r'groups', GroupViewSet)
router.register(r'gmembers', GMemberViewSet)


urlpatterns = [
    path('', include(router.urls)), 
]
