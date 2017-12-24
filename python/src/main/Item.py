class Item(object):
    def __init__(self, person_email, name, price, priority, hyperlink):
        self.person_email = person_email
        self.name = name
        self.price = price
        self.priority = priority
        self.hyperlink = hyperlink

    def print_price(self):
        print("The price of this item is %s big ones" % self.price)



