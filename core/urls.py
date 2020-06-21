from django.urls import path
from .views import (
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    AddCouponView,
    CheckoutView,
    HomeView,
    ItemDetailView,
    OrderSummaryView,
    PaymentView,
    RequestRefundView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]
