from django.contrib import admin
from django.urls import path, include

app_name = 'pydockapp'

urlpatterns = [
    path('pydockapp/', include('pydockapp.urls')),
    path('admin/', admin.site.urls),
]
