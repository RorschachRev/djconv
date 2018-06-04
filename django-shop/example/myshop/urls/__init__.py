# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from shop.views.auth import PasswordResetConfirm
from cms.sitemaps import CMSSitemap
from myshop.sitemap import ProductSitemap
from mydj import views
from django.contrib.auth import views as auth_views

sitemaps = {'cmspages': CMSSitemap,
            'products': ProductSitemap}


def render_robots(request):
    permission = 'noindex' in settings.ROBOTS_META_TAGS and 'Disallow' or 'Allow'
    return HttpResponse('User-Agent: *\n%s: /\n' % permission, content_type='text/plain')

i18n_urls = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/?$',
        PasswordResetConfirm.as_view(template_name='myshop/pages/password-reset-confirm.html'),
        name='password_reset_confirm'),
    url(r'^', include('cms.urls')),
)
urlpatterns = [
    url(r'^robots\.txt$', render_robots),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^$',  views.index, name='base'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'pages/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'pages/logout.html'}, name='logout'),
    url(r'^expo.html$', views.expo, name='expo'),
    url(r'^profile.html$', views.update_profile, name='profile'),
    url(r'^shop.html$', views.shop, name='shop'),
    url(r'^expomap.html$', views.expomap, name='expomap'),
    url(r'^edit.html$', views.edit, name='edit'),
    #url(r'^admin/', admin.site.urls),
    url(r'^signup.html$', views.signup, name='signup'),
]
if settings.USE_I18N:
    urlpatterns.extend(i18n_patterns(*i18n_urls))
else:
    urlpatterns.extend(i18n_urls)
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
