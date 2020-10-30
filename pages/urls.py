from django.urls import path, include
from . import views
from django.conf.urls.static import static
from freesite import settings

urlpatterns = [
                  path('', views.main_page, name='main_page'),
                  path('sitemap/', views.site_map, name='site_map'),
                  path('<int:pk>/', views.page_by_pk, name='page_by_pk'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('<str:title>/', views.page_by_title, name='page_by_title'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
