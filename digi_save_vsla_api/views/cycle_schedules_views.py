# views/cycle_schedules_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleSchedules
from digi_save_vsla_api.serializers import CycleSchedulesSerializer

@api_view(['GET', 'POST'])
def cycle_schedules_list(request):
    if request.method == 'GET':
        cycle_schedules = CycleSchedules.objects.all()
        serializer = CycleSchedulesSerializer(cycle_schedules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CycleSchedulesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cycle_schedules_detail(request, pk):
    try:
        cycle_schedule = CycleSchedules.objects.get(pk=pk)
    except CycleSchedules.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleSchedulesSerializer(cycle_schedule)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CycleSchedulesSerializer(cycle_schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cycle_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
