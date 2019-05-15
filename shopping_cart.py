class ShoppingCart():
    # write your code here
    def __init__(self, emp_discount=None):
        self.employee_discount = emp_discount
        self.total = 0
        self.items = []

    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total

    def mean_item_price(self):
        mean_price = self.total/len(self.items)
        return mean_price

    def median_item_price(self):
        all_items_price = [item['price'] for item in self.items]
        len_items_price = len(all_items_price)
        middle_point = int(len_items_price/2)
        if len_items_price % 2 != 0:
            median = all_items_price[middle_point]
        else:
            median = (all_items_price[middle_point] + all_items_price[middle_point - 1])/2
        return median


    def apply_discount(self):
       if self.employee_discount:
           discount = 1 - self.employee_discount/100
           discounted_total = self.total * discount
           return discounted_total
       else:
           return "Sorry, there is no discount to apply to your cart :("


    def void_last_item(self):
        if self.items:
            pop_last_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= pop_last_item['price']
