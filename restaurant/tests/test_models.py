from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class BookingModelTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=datetime(2026, 11, 2, 18, 0, 0)
        )
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 4)
