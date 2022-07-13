from tkinter import SE
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Api.serializers import AuthSerializer
import random

# Create your views here.


class AuthView(APIView):
    def get(self,request):
        try:
            Key = random.randint(100000,999999)
            return Response({"msg":"Token genarated successfully","token":Key,"status":status.HTTP_201_CREATED})
        except:
            return Response({"msg":"Somthing went worong","token":"No token has been genarated","status":status.HTTP_400_BAD_REQUEST})

    def post(self,request):
        Serializer = AuthSerializer(data=request.data)
        if Serializer.is_valid(raise_exception=True):
            Resp = Serializer.Validation(validated_data=request.data)
            if Resp != None:
                return Response({"msg":"Authentication Scuccess","token":Resp,"status":status.HTTP_201_CREATED})

            return Response({"msg":"Not Authenticaticated","token":Resp,"status":status.HTTP_404_NOT_FOUND})

        return Response({"msg":"Serializer is not valid","token":"Token is not provided","status":status.HTTP_400_BAD_REQUEST})
        
            






