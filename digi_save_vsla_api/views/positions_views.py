# views/positions_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Positions
from digi_save_vsla_api.serializers import PositionsSerializer

@api_view(['GET', 'POST'])
def positions_list(request):
    if request.method == 'GET':
        positions = Positions.objects.all()
        serializer = PositionsSerializer(positions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PositionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def positions_detail(request, pk):
    try:
        position = Positions.objects.get(pk=pk)
    except Positions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PositionsSerializer(position)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PositionsSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
