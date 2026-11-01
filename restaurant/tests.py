# Re-export unit tests for Django's default test runner
from .tests.test_models import MenuItemTest, BookingModelTest
from .tests.test_views import MenuViewTest

__all__ = ['MenuItemTest', 'BookingModelTest', 'MenuViewTest']
