# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products_prices = {product:price for product, price in zip(products, prices)}
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        
        total = 0

        # looping throught the customer's products and calculating total
        for prod, qty in zip(product, amount):
            total = total + (self.products_prices[prod] * qty)

        self.customer_count += 1
        if self.customer_count == self.n:
            total = total * ((100 - self.discount) / 100)
            self.customer_count = 0

        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)