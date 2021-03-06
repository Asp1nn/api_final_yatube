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
    'posts',
    PostViewSet,
    basename='posts')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router_v1.register(
    r'group',
    GroupViewSet,
    basename='group')
router_v1.register(
    r'follow',
    FollowViewSet,
    basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/token/', include(URL_TOKEN)),
]
