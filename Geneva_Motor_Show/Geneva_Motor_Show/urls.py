from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
    path('brand/', include('Brand.urls')),
    path('car/', include('cars.urls')),
    path('category/', include('categories.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
