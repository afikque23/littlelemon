from django.db import models


# Model for Menu items
# Used by MenuItemsView and SingleMenuItemView in the Capstone API
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    @property
    def name(self):
        return self.title


# MenuItem alias for compatibility with test imports and references
MenuItem = Menu


# Model for Table Bookings / Reservations
# Used by BookingViewSet in the Capstone API
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {str(self.booking_date)}"

    @property
    def first_name(self):
        return self.name
