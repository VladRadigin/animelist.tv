from django.contrib import admin
from django.urls import path, include
from myList.views import index

urlpatterns = [
    path('mylist/', include('myList.urls')),
    path('admin/', admin.site.urls),
]
