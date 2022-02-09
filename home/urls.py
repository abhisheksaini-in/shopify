from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from home import views

urlpatterns = [
    
    path('', views.ProductView.as_view(), name='home'),
    
    
    
    
    path('product-detail/<slug:url>', views.ProductDetailView.as_view(),name='product-detail' ),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
    path('appliances/', views.appliances, name='appliances'),
    path('appliances/<slug:data>', views.appliances, name='appliancesdata'),
    
    path('menfashion/', views.menfashion, name='menfashion'),
    path('menfashion/<slug:data>', views.menfashion, name='menfashiondata'),
    
    path('womenfashion/', views.womenfashion, name='womenfashion'),
    path('womenfashion/<slug:data>', views.womenfashion, name='womenfashiondata'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('add-to-cart/', views.addtocart, name='add-to-cart'),
    path('items-in-cart/', views.items_in_cart, name='items-in-cart'),
    path('pluscart/', views.plus_cart, name='plus-cart'),
    path('minuscart/', views.minus_cart, name='minus-cart'),
    path('removecart/', views.remove_cart, name='remove-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('search/', views.search, name='search'),
    
   
    
    path('buy/', views.buy_now, name='buy-now'),
    
   
    path('orders/', views.orders, name='orders'),
    
    
    
    
    
    
    
    
    path('tinymce/', include('tinymce.urls')),
    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
