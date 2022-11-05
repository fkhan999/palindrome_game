from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json
from .serializers import *
from game.models import palindrome
import random

# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def startgame(request,*args,**kwargs):
    serializer=palindromeSerializers(data={"user":str(request.user)})
    if not serializer.is_valid():
        return Response({'error':serializer.errors,"message":"Please provide correct data"},status=403)
    serializer.save()
    print(serializer.data)
    return Response({"game":serializer.data,"message":"game successfully created"})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getBoard(request,id,*args,**kwargs):
    obj=palindrome.objects.filter(id=id,user=str(request.user))
    serializer=palindromeSerializers(obj,many=True)
    return Response({"games":serializer.data,"message":"game succesfully fetched"})



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateBoard(request,id,*args,**kwargs):
    try:
        obj=palindrome.objects.get(id=id,user=str(request.user))
        if len(obj.string)>=6:
            return Response({"game":id,"message":"string cannot be appended as it length its length cannot be more than 6","string":obj.string,"ispalindrome":obj.string==obj.string[::-1]})

    except:
        return Response({ "message":"no game with id " +str(id)+" belonging to user "+str(request.user)})

    try:
        request_body=json.loads(request.body)
        string_req=request_body['append']
        if len(string_req)!=1:
            return Response({ "message":"length of append string should be 1"})
        if not string_req.isalpha() or not string_req.islower():
            return Response({ "message":"string should be alphabet a-z"})


    except:
        return Response({ "message":"please provide correct data"})

    r=str(random.randint(0,9))
    obj.string+=string_req+r
    obj.save()
    if len(obj.string)==6 and obj.string==obj.string[::-1]:
        return Response({"games":id,"message":"string successfully appended and it is a palindrome","string":obj.string})
    elif len(obj.string)==6 and obj.string!=obj.string[::-1]:
        return Response({"games":id,"message":"string successfully appended and it is not a palindrome","string":obj.string})


    return Response({"games":id,"message":"string successfully appended","string":obj.string})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getGames(request,*args,**kwargs):
    obj=palindrome.objects.filter(user=str(request.user))
    serializer=palindromeSerializers(obj,many=True)
    return Response({"games":serializer.data,"message":"games successfully fetched"})

    