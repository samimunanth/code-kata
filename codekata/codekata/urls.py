
from django.contrib import admin
from django.urls import path
from demystdata.views import fetch_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', fetch_todo,name='todo'),
]
