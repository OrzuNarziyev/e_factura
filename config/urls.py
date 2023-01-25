"""config URL Configuration

The `urlpatterns` list routes URLs to prod_views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function prod_views
    1. Add an import:  from my_app import prod_views
    2. Add a URL to urlpatterns:  path('', prod_views.home, name='home')
Class-based prod_views
    1. Add an import:  from other_app.prod_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('factura.urls')),
    path('admin/', admin.site.urls),

]
