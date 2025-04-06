from django.urls import include, path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/', include([
        path('new/', PostCreateView.as_view(), name='post_create'),
        path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    ])),
]
