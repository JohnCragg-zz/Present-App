class Person(object):
    def __init__(self, first_name, second_name, age, description):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.description = description

    def say_hello(self):
        print "hello %s %s !" % (self.first_name, self.second_name)
