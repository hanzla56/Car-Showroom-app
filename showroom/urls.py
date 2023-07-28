from django.contrib import admin
from django.urls import path
from . import views # added manually

# below two lines added manually
from django.conf.urls.static import static
from django.conf import settings


app_name = 'showroom' # added manually

urlpatterns = [
    path("admin", admin.site.urls , name="admin"),
    path("", views.home , name='home'),
    path("<str:brand_name>" , views.models_page , name='model_page'),
    path("team/", views.team_page , name='team'),
    path("stock/", views.stock_page , name='stock')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Added manually