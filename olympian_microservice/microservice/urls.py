from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
# from olympians.views import CompanyListView, CompanyDetailView
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.urls import path, include
from olympians import views
from rest_framework.authtoken import views




schema_view = get_swagger_view(title='Company')

urlpatterns = [  
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('', include('olympians.urls', namespace="olympians")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('olympians-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]