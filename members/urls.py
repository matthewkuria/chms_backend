from django.urls import path
from .views import MemberDetailView

urlpatterns = [
    path('member-detail/', MemberDetailView, basename='member-detail')
]
