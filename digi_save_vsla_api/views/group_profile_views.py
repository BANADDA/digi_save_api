from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import GroupProfile
from digi_save_vsla_api.serializers import GroupProfileSerializer

@api_view(['GET', 'POST'])
def group_profile_list(request):
    print("Received data:", request.data)
    if request.method == 'GET':
        group_profiles = GroupProfile.objects.all()
        serializer = GroupProfileSerializer(group_profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def group_profile_detail(request, pk):
    try:
        group_profile = GroupProfile.objects.get(pk=pk)
    except GroupProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupProfileSerializer(group_profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupProfileSerializer(group_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
