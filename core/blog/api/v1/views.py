from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def postList(request):
#     if request.method == 'GET':
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data) # must specify argument by data =

#         # validation must be done. there is 2 ways to validate. one is if statement and other is raise exception
        
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data)
#         # else:
#         #     return Response(serializer.errors)

#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class PostList(APIView):
#     # getting a list of post and creating a new post

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request):
#         # retrieving a list of posts
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         # creating a post
#         serializer = PostSerializer(data=request.data) # must specify argument by data =
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def postDetail(request, id):
#     post = get_object_or_404(Post, pk=id, status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response({"detail":"Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)

#     # try:
#     # except Post.DoesNotExist:  # creating a 404 response / or do it with get_object_or_404 instead of get
#     #     return Response({'detail':'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)


# class PostDetail(APIView):
#     # getting detail of the post and edit plus deleting it

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request, id):
#         # retrieving the post data
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         # editing the post data
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         # deleting the post
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"detail":"Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    

# class PostList(ListCreateAPIView):
#     # getting a list of post and creating a new post
#     queryset = Post.objects.filter(status=True)
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     # getting detail of the post and edit plus deleting it
#     queryset = Post.objects.filter(status=True)
#     # lookup_field = 'id' # or make the argument in the url pk instead of id
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer


class PostViewSets(viewsets.ViewSet):
    queryset = Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        serializer =  self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, *args, **kwargs):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer =  self.serializer_class(post)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass