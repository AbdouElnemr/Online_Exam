from django.contrib import admin
from django.urls import path, include
from account.views import login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('account/', include('account.urls')),
    path('exam/', include('exam.urls')),
]
