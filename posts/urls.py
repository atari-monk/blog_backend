from django.urls import include, path
from .views import PostListView, PostDetailView, PostCreateView, SignUpView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('post/', include([
        path('new/', PostCreateView.as_view(), name='post_create'),
        path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
        path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    ])),
]
