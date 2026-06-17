from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django.urls import include, path
from django.urls import re_path

from apps.portfolio import views as portfolio_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.portfolio.urls")),
    path("health/", portfolio_views.health_check, name="health"),
    path("robots.txt", portfolio_views.robots_txt, name="robots_txt"),
    path("sitemap.xml", portfolio_views.sitemap_xml, name="sitemap_xml"),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
