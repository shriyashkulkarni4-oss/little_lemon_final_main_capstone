from datetime import date, time

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Booking, MenuItem


class MenuApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = MenuItem.objects.create(title="Greek Salad", price="12.50", inventory=20)

    def test_menu_is_publicly_readable(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], "Greek Salad")

    def test_menu_changes_require_authentication(self):
        response = self.client.post(
            "/restaurant/menu/", {"title": "Bruschetta", "price": "8.00", "inventory": 10}
        )
        self.assertEqual(response.status_code, 401)


class BookingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username="reviewer", password="safe-pass-123")

    def test_booking_list_requires_authentication(self):
        response = self.client.get("/restaurant/booking/tables/")
        self.assertEqual(response.status_code, 401)

    def test_authenticated_user_can_create_booking(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            "/restaurant/booking/tables/",
            {
                "name": "Alex Morgan",
                "no_of_guests": 2,
                "booking_date": date.today().isoformat(),
                "booking_time": time(19, 0).isoformat(timespec="minutes"),
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.get().created_by, self.user)


class AuthenticationTests(TestCase):
    def test_registration_creates_user_and_password_is_hashed(self):
        response = self.client.post(
            "/api/register/",
            {"username": "new-guest", "email": "guest@example.com", "password": "strong-pass-123"},
        )
        self.assertEqual(response.status_code, 201)
        user = get_user_model().objects.get(username="new-guest")
        self.assertTrue(user.check_password("strong-pass-123"))
