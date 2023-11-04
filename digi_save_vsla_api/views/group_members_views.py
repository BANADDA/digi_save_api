# views/group_members_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import GroupMembers
from digi_save_vsla_api.serializers import GroupMembersSerializer

@api_view(['GET', 'POST'])
def group_members_list(request):
    if request.method == 'GET':
        group_members = GroupMembers.objects.all()
        serializer = GroupMembersSerializer(group_members, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupMembersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def group_members_detail(request, pk):
    try:
        group_member = GroupMembers.objects.get(pk=pk)
    except GroupMembers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupMembersSerializer(group_member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupMembersSerializer(group_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
