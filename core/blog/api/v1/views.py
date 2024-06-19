from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view()
def postList(request):
    posts = Post.objects.filter(status=True)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view()
def postDetail(request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # try:
    # except Post.DoesNotExist:  # creating a 404 response / or do it with get_object_or_404 instead of get
    #     return Response({'detail':'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)