from django.contrib import admin

from .models import Booking, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "inventory")
    search_fields = ("title",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "booking_date", "booking_time", "no_of_guests", "created_by")
    list_filter = ("booking_date",)
    search_fields = ("name",)
