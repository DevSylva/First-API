
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
     openapi.Info(
     title="Freit App API",
     default_version='v1',
     description="Test description",
     terms_of_service="https://www.ourapp.com/policies/terms/",
     contact=openapi.Contact(email="contact@snippets.local"),
     license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
]
