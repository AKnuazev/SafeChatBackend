from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # The admin panel url
    path('admin/', admin.site.urls),

    # The API urls
    path('api/v1/', include('accounts.urls')),  # urls for account related API endpoints
    path('api/v1/', include('chats.urls')),  # urls for chat related API endpoints

    # The authentication urls
    path('api-auth/', include('rest_framework.urls')),  # Login and logout views for the browsable API
]