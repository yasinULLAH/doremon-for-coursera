
from django.test import TestCase
from .models import MenuItem, TableBooking

class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(name="Pasta", description="Italian Pasta", price=10.00)

    def test_menu_item_creation(self):
        item = MenuItem.objects.get(name="Pasta")
        self.assertEqual(item.price, 10.00)

class TableBookingTest(TestCase):
    def setUp(self):
        TableBooking.objects.create(
            name="John Doe", email="john@example.com", date="2024-12-01", time="18:30", num_guests=4
        )

    def test_booking_creation(self):
        booking = TableBooking.objects.get(name="John Doe")
        self.assertEqual(booking.num_guests, 4)
