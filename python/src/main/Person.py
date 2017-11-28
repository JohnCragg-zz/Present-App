class Person(object):
    def __init__(self, personal_id, email, first_name, second_name):
        self.personal_id = personal_id
        self.email = email
        self.first_name = first_name
        self.second_name = second_name


    def say_hello(self):
        print ("hello %s %s !" % (self.first_name, self.second_name))
