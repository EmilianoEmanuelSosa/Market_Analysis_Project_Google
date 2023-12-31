from django.urls import path, re_path
from .api import RestaurantViewSet,UserViewSet, ReviewViewSet

urlpatterns = [
    # Otras rutas...
    path('restaurant', RestaurantViewSet.as_view({'post': 'get_restaurant'}), name='get_restaurant'),
    path('restaurantes_en_radio/<str:restaurant_id>/<str:radius_km>/', RestaurantViewSet.as_view({'get': 'get_restaurants_in_radius'}), name='restaurants-in-radius'),
    path('restaurantes_reviews/<str:restaurant_id>/', RestaurantViewSet.as_view({'get': 'get_reviews_for_restaurant'}), name='restaurant-reviews'),
    path('usuarios/<str:user_id>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
    path('interprete-languaje/', ReviewViewSet.as_view({'post':'interpreter'}))
] 