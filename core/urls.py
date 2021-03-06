# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView
# from rest_framework.authtoken import views
from apps.simc.views import CharacterView, CardView, MonsterView, BattleView, BattleSimc, BattleIsExist

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path("api/", include("apps.core.urls")),  # UI Kits Html files
    path("", include("apps.authentication.urls")),  # Auth routes - login / register
    path("", include("apps.app.urls")),  # UI Kits Html files
]

urlpatterns += [
                   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                   # path('api-token-auth/', views.obtain_auth_token),
                   url(r'^favicon\.ico$', RedirectView.as_view(
                       url='/core/static/images/favicon.ico'))
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
