# views/assigned_positions_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import AssignedPositions
from digi_save_vsla_api.serializers import AssignedPositionsSerializer

@api_view(['GET', 'POST'])
def assigned_positions_list(request):
    if request.method == 'GET':
        assigned_positions = AssignedPositions.objects.all()
        serializer = AssignedPositionsSerializer(assigned_positions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AssignedPositionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def assigned_positions_detail(request, pk):
    try:
        assigned_position = AssignedPositions.objects.get(pk=pk)
    except AssignedPositions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssignedPositionsSerializer(assigned_position)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AssignedPositionsSerializer(assigned_position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        assigned_position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

