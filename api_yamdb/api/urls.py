from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "api"

router_v1 = routers.DefaultRouter()
router_v1.register("titles", views.TitleViewSet, basename="title")
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews",
    views.ReviewViewSet,
    basename="reviews",
)
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    views.CommentViewSet,
    basename="comments",
)
router_v1.register("users", views.UserViewSet, basename="users")
router_v1.register("genres", views.GenreViewSet, basename="genres")
router_v1.register(
    "categories", views.CategoryViewSet, basename="categories"
)
auth_urls = [
    url('token/', views.signup_confirm),
    url('signup/', views.signup),
]
urlpatterns = [
    path("v1/auth/", include(auth_urls)),
    path("v1/", include(router_v1.urls)),
]
