class ShoppingCart:
    def __init__(self):
        self.prices = []

    price = 0

    '''
    the goal is to remove the field above, using a list of prices instead:
    def __init__(self):
        self.prices = []
    '''

    def add(self, price):
        self.prices.append(price)

    def calculate_total_price(self):
        return self.calculate_total_price_parallel()

    def calculate_total_price_parallel(self):
        total = 0
        for price in self.prices:
            total += price
        return total

    def has_discount(self):
        return self.has_discount_parallel()

    def has_discount_parallel(self):
        for price in self.prices:
            if price >= 100:
                return True
        return False

    def number_of_products(self):
        return self.number_of_products_parallel()

    def number_of_products_parallel(self):
        return len(self.prices)


class SomeConsumer():
    def do_stuff():
        shoppingCart = ShoppingCart()
        shoppingCart.add(100)
        print("other consumer", shoppingCart.calculate_total_price())


if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    print("number of products:", shoppingCart.number_of_products())
    print("total price:", shoppingCart.calculate_total_price())
    print("has discount:", shoppingCart.has_discount())
