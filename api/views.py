from .models import Todo
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer


class TodoList(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

#read - create - update - delete
@api_view(['POST'])
def CreateTask(request):
    serializer=TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['POST'])
def UpdateTask(request,pk):
    tasks=Todo.objects.get(id=pk)
    serializer=TodoSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTask(request, pk):
    task=Todo.objects.get(id=pk)
    task.delete()
    return Response('Object has deleted successfully!')    

