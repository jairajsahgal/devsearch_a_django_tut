from django.contrib import admin
from django.urls import path, include
from projects import models


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))

]
