from django.urls import path
from .views import (
    RestaurantListCreateView,
    RestaurantDetailView,

    comment_create_view,
    CommentUpdateDeleteView,
    MyPostView,
)

urlpatterns = [
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
      # bu url asosan o'sha product ni to'liq ko'rish uchun
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
      # bu url asosan o'sha product uchun comment yozish
    path('restaurants/<int:pk>/comments/', comment_create_view, name='comment-create'),
      # bu url asosan comment ni delete va update qilish uchun
    path('comments/<int:pk>/', CommentUpdateDeleteView.as_view(), name='comment-update-delete'),
      # bu url asosan mening postlarim uchun
    path('my-posts/', MyPostView.as_view(), name='my-posts'),
]
