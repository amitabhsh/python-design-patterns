"""Builder Patter in python
Although there are easier approaches like passing the options as arugments, i went with the traditional "bythe book" appraoch.discount

Build a complex Object using simple steps. In this example, i am building an order on a shopping website with simple steps
OrderBuilder.defaultbuild() - creates an Order Builder Object()
withitems() - sets the items for this builder
costs() - sets the cost
minusdiscount - sets the discount for the order
"""
__author__ = 'amit'


class Order(object):
    def __init__(self):
        self.orderid = None
        self.items = None
        self.cost = 0.0
        self.discount = 0.0


class OrderBuilder(object):
    def __init__(self):
        self.order = None

    def withitems(self, items):
        self.order.items = items
        return self

    def costs(self, cost):
        self.order.cost = cost
        return self

    def minusdiscount(self, discount):
        self.order.discount = discount
        return self

    def defaultbuild(self):
        self.order = Order()
        return self

    def build(self):
        return self.order

if __name__ == '__main__':
    builder = OrderBuilder()
    customorder = builder.defaultbuild().withitems("Amazon Kindle").costs(100.0).minusdiscount(2.5).build()
    print "New Order for {0} costs {1} with discount {2}".format(customorder.items, customorder.cost, customorder.discount)
    assert customorder.discount == 2.5
    assert customorder.items == "Amazon Kindle"





