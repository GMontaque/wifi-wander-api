from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Comments
from .serializers import CommentSerializer
from wifi_wander_api.permissions import IsOwnerOrReadOnly


# View to handle listing all comments and creating new comments
class CommentList(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(CommentList, self).get_permissions()

    def get(self, request):
        wifi_location_id = request.query_params.get('wifi_location', None)

        if wifi_location_id:
            comments = Comments.objects.filter(
                wifi_location_id=wifi_location_id
            )
        else:
            comments = Comments.objects.all()

        serializer = CommentSerializer(
            comments, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to handle retrieving, updating, or deleting a specific comment
class CommentDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            comment = Comments.objects.get(pk=pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Comments.DoesNotExist:
            raise Http404

    # Handle GET request to retrieve a specific comment
    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, context={'request': request})
        return Response(serializer.data)

    # Handle PUT request to update a specific comment
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(
            comment, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle DELETE request to delete a specific comment
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(
            {"msg": "Comment Deleted"}, status=status.HTTP_204_NO_CONTENT
        )
