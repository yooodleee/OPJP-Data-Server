"""
URL configuration for OPJP_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("book_registration/", include('book_registration.urls')),
    path("bookmark/", include('bookmark.urls')),
    path("books/", include('books.urls')),
    path("cart/", include('cart.urls')),
    path("crawl", include('crawl.urls')),
    path("kakao_account/", include('kakao_account.urls')),
    path("kakao_account_profile/", include('kakao_account_profile.urls')),
    path("kakao_authentication/", include('kakao_authentication.urls')),
    path("normalization/", include('normalization.urls')),
    path("order/", include('order.urls')),
    path("payment/", include('payment.urls')),
    path("redis_cache/", include('redis_cache.urls')),
    path("regression/", include('regression.urls')),
    path("resource/", include('resource.urls')),
    path('subscription/', include('subscription.urls')),
]
