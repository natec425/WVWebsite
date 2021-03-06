"""WVWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from WVWebsite.app.views import (
    render_page,
    home,
    PostCreate,
    PostUpdate,
    PostDelete,
    logout_view,
    UpdateView,
    AboutUpdate,
    OrdinanceCreate,
    OrdinanceUpdate,
    OrdinanceDelete,
)
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth import logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="Home"),
    path("tinymce/", include("tinymce.urls")),
    path("accounts/", include("allauth.urls")),
    path("post/create/", PostCreate.as_view(), name="create_post"),
    path("post/create/<int:pk>/update", PostUpdate.as_view(), name="update_post"),
    path("post/<int:pk>/delete/", PostDelete.as_view(), name="delete_post"),
    path("about/<int:pk>/update", AboutUpdate.as_view(), name="update_about"),
    path("post/ordinance/", OrdinanceCreate.as_view(), name="create_ordinance"),
    path(
        "post/ordinance/<int:pk>/update",
        OrdinanceUpdate.as_view(),
        name="update_ordinance",
    ),
    path(
        "ordinance/<int:pk>/delete/", OrdinanceDelete.as_view(), name="delete_ordinance"
    ),
    path("logout", logout_view, name="logout"),
]
