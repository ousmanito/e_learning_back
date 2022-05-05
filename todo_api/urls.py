from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo_api.views import TaskViewSet, UserViewSet
from rest_framework.authtoken import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'task', TaskViewSet,basename="task")
router.register(r'user', UserViewSet, basename='user' )

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

