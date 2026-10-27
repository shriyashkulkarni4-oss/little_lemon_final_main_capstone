from django.conf import settings
from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )

    class Meta:
        ordering = ["booking_date", "booking_time"]

    def __str__(self):
        return f"{self.name} — {self.booking_date} {self.booking_time}"
