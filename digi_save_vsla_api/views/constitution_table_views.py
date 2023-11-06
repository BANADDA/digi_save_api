from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import ConstitutionTable
from digi_save_vsla_api.serializers import ConstitutionTableSerializer

@api_view(['GET', 'POST'])
def constitution_table_list(request):
    print("Received data:", request.data)
    if request.method == 'GET':
        constitution_tables = ConstitutionTable.objects.all()
        serializer = ConstitutionTableSerializer(constitution_tables, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print("Received data:", request.data)
        serializer = ConstitutionTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def constitution_table_detail(request, pk):
    try:
        constitution_table = ConstitutionTable.objects.get(pk=pk)
    except ConstitutionTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConstitutionTableSerializer(constitution_table)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConstitutionTableSerializer(constitution_table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        constitution_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
