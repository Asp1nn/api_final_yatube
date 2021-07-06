from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from .models import Post, Group, Follow
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer, GroupSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        group_filter = self.request.query_params.get('group', None)
        if group_filter is not None:
            queryset = queryset.filter(group=group_filter)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(
            Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return serializer.save(author=self.request.user,
                               post_id=post.id)


class FollowViewSet(CreateModelMixin, ListModelMixin, viewsets.GenericViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.filter()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
