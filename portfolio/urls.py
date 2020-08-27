from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from main import urls as main_urls

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(main_urls)),
	#path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)