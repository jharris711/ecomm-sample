from django.contrib import admin
from .models import (
    Address,
    Coupon,
    Item,
    OrderItem,
    Order,
    Payment,
    Refund,
    UserProfile,
)


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_granted=True)


make_refund_accepted.short_description = 'Update to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ref_code',
        'ordered',
        'ordered_date',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
        'billing_address',
        'shipping_address',
        'payment',
        'coupon',
    ]
    list_display_links = [
        'user',
        'billing_address',
        'shipping_address',
        'payment',
        'coupon',
    ]
    list_filter = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
    ]
    search_fields = [
        'user__username',
        'ref_code',
    ]
    actions = [
        make_refund_accepted,
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'address_type',
        'street_address',
        'apartment_address',
        'country',
        'zipcode',
        'default',
    ]
    list_filter = [
        'default',
        'address_type',
        'country',
    ]
    search_fields = [
        'user',
        'street_address',
        'apartment_address',
        'city',
        'zipcode',
    ]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
