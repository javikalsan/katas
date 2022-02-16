class ShoppingCart:
    def __init__(self):
        self.prices = []

    def add(self, price):
        self.prices.append(price)

    def calculate_total_price(self):
        total = 0
        for price in self.prices:
            total += price
        return total

    def has_discount(self):
        for price in self.prices:
            if price >= 100:
                return True
        return False

    def number_of_products(self):
        return len(self.prices)


class SomeConsumer:
    def do_stuff():
        shopping_cart = ShoppingCart()
        shopping_cart.add(100)
        print("other consumer", shopping_cart.calculate_total_price())


if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    print("number of products:", shoppingCart.number_of_products())
    print("total price:", shoppingCart.calculate_total_price())
    print("has discount:", shoppingCart.has_discount())
