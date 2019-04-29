from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name='home'),
    # blog
    path('blog/', include('blogapp.urls')),
    # portfolio
    path('blog/portfolio/', include('portfolio.urls')),
    # accounts
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
