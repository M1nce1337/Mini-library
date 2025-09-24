from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('app/', include("app.urls")),
    path('users/', include("users.urls", namespace="users")),
    path('admin/', admin.site.urls),
]
