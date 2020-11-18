from django.urls import path, include
from . import views
from django.conf.urls.static import static
from freesite import settings

urlpatterns = [
                  path('', views.main_page, name='main_page'),
                  path('pagelist/', views.page_list, name='page_list'),
                  path('page/<int:pk>/', views.page, name='page'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('menu/<int:pk>/', views.menu_page, name='menu_page'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
