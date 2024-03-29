import unittest
import method
import field

NORMAL_USER_ROLE = 'normal'
ADMIN_USER_ROLE = 'admin'
ADMIN_USER_ID = 12345
A_NORMAL_USER_ID = 11111


class AuthenticatorTests(unittest.TestCase):
    def test_administrator_is_always_authenticated(self):
        service = method.AuthenticationService()
        self.assertTrue(service.is_authenticated(ADMIN_USER_ID, ADMIN_USER_ROLE))

    def test_normal_user_is_not_authenticated_initially(self):
        service = method.AuthenticationService()
        self.assertFalse(service.is_authenticated(A_NORMAL_USER_ID, NORMAL_USER_ROLE))


class ShoppingCartTests(unittest.TestCase):
    def test_cart_have_an_items_prices_list(self):
        shopping_cart = field.ShoppingCart()

        shopping_cart.add(10)
        shopping_cart.add(10)

        self.assertEqual(2, len(shopping_cart.prices))

    def test_the_total_price_of_the_cart_is_the_sum_of_prices(self):
        shopping_cart = field.ShoppingCart()

        shopping_cart.add(10)
        shopping_cart.add(10)

        self.assertEqual(20, shopping_cart.calculate_total_price())

    def test_has_discount_when_contains_at_least_one_premium_item(self):
        shopping_cart = field.ShoppingCart()

        shopping_cart.add(100)
        shopping_cart.add(20)

        self.assertTrue(shopping_cart.has_discount())

    def test_doesnt_have_discount_when_all_its_items_are_cheap(self):
        shopping_cart = field.ShoppingCart()

        shopping_cart.add(10)

        self.assertFalse(shopping_cart.has_discount())


if __name__ == "__main__":
    unittest.main()
