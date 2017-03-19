class Guy:

    def __init__(self):
        self.__age = 10

    def get_fullname(self, first_name, last_name):
        return first_name + ' ' + last_name

    def get_age(self):
        return self.__age

    @staticmethod
    def get_class_name():
        return Guy.__name__
