from django.urls import path, include

from django.contrib import admin

from rest_framework.routers import DefaultRouter

from django.conf.urls import (
    url
)

admin.autodiscover()

from watcher import views

router = DefaultRouter()
router.register(r'pushes', views.PushViewSet)

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", views.index, name="index"),
    path("db/", views.db, name="db"),
    path("admin/", admin.site.urls),
    url(r'^', include(router.urls)),
]
