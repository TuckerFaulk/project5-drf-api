from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MasterTask
from .serializers import MasterTaskSerializer


class MasterTaskList(APIView):

    serializer_class = MasterTaskSerializer

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
