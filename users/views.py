from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deactivate_user(request):
    user = request.user
    user.is_active = False
    user.save()
    return Response({'message': 'User deactivated successfully.'}, status=200)
