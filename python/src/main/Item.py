class Item(object):
    def __init__(self, person_email, name, price, priority, hyperlink):
        self.person_email = person_email
        self.name = name
        self.price = price
        self.priority = priority
        self.hyperlink = hyperlink

    def serialize(self):
        return {
            'person_email': self.person_email,
            'name': self.name,
            'price': self.price,
            'priority': self.priority,
            'hyperlink': self.hyperlink
        }

