from django.shortcuts import render
from rest_framework.decorators import api_view
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json
from .serializers import *



"""
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def home(request,*args,**kwargs):
    b=request.body
    print(request.GET,b,dict(request.GET))
    try:
        b=json.loads(b)
    except:
        b={"msg-error":str(b)}
        pass
    b['headers']=dict(request.headers)
    b['data']=dict(request.GET)
    print(dict(request.GET))
    b['content_type']=request.content_type
    return Response(b)
"""
@api_view(['POST'])
def createUser(request,*args,**kwargs):
    serializer=UserSerializers(data=request.data)
    if not serializer.is_valid():
        return Response({'error':serializer.errors,"message":"Please provide correct data"},status=403)
    serializer.save()
    return Response({"message":"User created succesfully"},status=200)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteUser(request,*args,**kwargs):
    obj=User.objects.get(username=request.user)
    obj.delete()
    return Response({"message":"User deleted succesfully"},status=200)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateUser(request,*args,**kwargs):
    try:
        obj=User.objects.get(username=request.user)
        obj.set_password(json.loads(request.body)['new_password'])
        obj.save()
    except:
        return Response({"message":"Please provide new password"},status=403)
    return Response({"message":"password updated succesfully"},status=200)

