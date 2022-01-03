from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Maxwell Muhanda Admin'
admin.site.index_title = 'Howdy Boss'

urlpatterns = [
    path('manager/', admin.site.urls),
    path('', include('blog.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('summernote/', include('django_summernote.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
