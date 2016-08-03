from django.conf.urls import include, url

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

urlpatterns = (
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
)
