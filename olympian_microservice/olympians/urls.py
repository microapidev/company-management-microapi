from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from olympians.views import CompanyList, CompanyDetail, UserList, UserDetail
from django.conf.urls import url
from olympians import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'olympians'

urlpatterns = [ 
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'), 
    path('company/', views.CompanyList.as_view(), name='company-list'),
    path('company/<int:pk>/',  views.CompanyDetail.as_view(), name='company-detail'),
    path('company/<int:pk>/highlight/', views.CompanyHighlight.as_view(), name='company-highlight'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)