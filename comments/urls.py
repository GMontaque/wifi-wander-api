from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentList.as_view(), name='comments-list'),
    path(
        'comments/<int:pk>/',
        views.CommentDetail.as_view(),
        name='comments-detail'
    ),
]
