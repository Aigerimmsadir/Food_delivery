from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from main.serializers import UserModelSerializer


@api_view(['POST'])
@csrf_exempt
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid data'})

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})
class UserCreate(APIView):

    def post(self, request, format='json'):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)




