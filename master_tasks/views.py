from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MasterTask
from .serializers import MasterTaskSerializer


class MasterTaskList(APIView):

    serializer_class = MasterTaskSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        tasks = MasterTask.objects.all()
        serializer = MasterTaskSerializer(
            tasks, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = MasterTaskSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class MasterTaskDetail(APIView):
    """
    Detail individual master_tasks
    """
    serializer_class = MasterTaskSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            master_task = MasterTask.objects.get(pk=pk)
            self.check_object_permissions(self.request, master_task)
            return master_task
        except MasterTask.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        master_task = self.get_object(pk)
        serializer = MasterTaskSerializer(
            master_task, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        master_task = self.get_object(pk)
        serializer = MasterTaskSerializer(
            master_task, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
