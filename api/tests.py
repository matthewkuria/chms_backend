from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from api import views


token = Token.objects.get(user__username="mwangi@gmail.com")
client = APIClient()
# client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
client.force_authenticate(user=user)

class TestEvents(APITestCase):
    def setUp(self):
        self.client=APIClient()
        self.view=views.EventViewSet.as_view({'get':'list'})
        self.uri='/events/'        
   
    def test_list2(self):
        self.client.login(email="mwangi@gmail.com",password="testing321")
        response=self.client.get(self.uri)
        self.assertEqual(response.status_code,200,
        'ExpectedResponseCode200,received {0}instead.'
        .format(response.status_code)) 