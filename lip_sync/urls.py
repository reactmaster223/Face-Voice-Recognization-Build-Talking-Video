from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.home_view, name="video_upload"),
    path("admin/", admin.site.urls),
]


from django.conf.urls.static import static
from lip_sync import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
