from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('bot.urls')),
    path('chat/',include('bot.urls')),
    path('admin/', admin.site.urls),
]
