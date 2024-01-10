from rest_framework import status
from rest_framework.response import Response
from .models import Solves
from tests.models import Tests
from .serializers import SolveSerializers
from rest_framework.decorators import api_view

@api_view(['GET'])
def solves(request, pk):
    if request.method == 'GET':
        solve = Solves.objects.filter(user_id=pk).values_list('test', flat=True).distinct()
        return Response(solve, status=status.HTTP_200_OK)



@api_view(['POST'])
def add_solve(request):

    if request.method == 'POST':
        serializer = SolveSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)