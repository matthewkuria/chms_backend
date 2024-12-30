from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Member

   
class MemberPagination(PageNumberPagination):
    page_size = 7

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = MemberPagination
    permission_classes = [IsAuthenticated]
    


class MemberDetailView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]    

    def get_queryset(self):
        return Member.objects.filter(user=self.request.user)