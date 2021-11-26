from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from todos_app.views import TasksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TasksViewSet, basename="Tasks")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
