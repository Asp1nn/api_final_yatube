from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet

URL_TOKEN = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh')
]

router_v1 = routers.DefaultRouter()
router_v1.register(
    'v1/posts',
    PostViewSet,
    basename='posts')
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router_v1.register(
    r'v1/group',
    GroupViewSet,
    basename='group')
router_v1.register(
    r'v1/follow',
    FollowViewSet,
    basename='follow')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('token/', include(URL_TOKEN)),
]
