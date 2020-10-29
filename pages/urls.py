from django.urls import path, include
from . import views
from django.conf.urls.static import static
from freesite import settings

urlpatterns = [
                  path('', views.main_page, name='main_page'),
                  path('map/', views.site_map, name='site_map'),
                  path('page/<int:pk>/', views.show_page, name='show_page'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
