from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryList(APIView):
    """
    Lists all categories.
    Only admin users can list and create categories.
    Generic views have not been used within this instance to display the
    ability to be able to create class-based views.
    """

    serializer_class = CategorySerializer

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class CategoryDetail(APIView):
    """
    Detail individual categories.
    Retrieve, update or delete a category if admin user.
    Generic views have not been used within this instance to display the
    ability to be able to create class-based views.
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            self.check_object_permissions(self.request, category)
            return category
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
