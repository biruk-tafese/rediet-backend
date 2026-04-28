from django.urls import path, include

urlpatterns = [
    path("", include("apps.content.urls")),
    path("", include("apps.prayers.urls")),
    path("", include("apps.users.urls")),
]