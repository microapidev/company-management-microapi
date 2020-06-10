from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Api import views
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='OLYMPIANS')
urlpatterns = [
    url(r'^$', schema_view),   
    path('companies/', views.CompanyList.as_view(), name='listview'), 
    path('companies/<int:pk>', views.CompanyDetail.as_view(), name='detail'),
    path('admin/', admin.site.urls),   
] 
