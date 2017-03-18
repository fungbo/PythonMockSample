class Person:
    def __init__(self):
        super().__init__()
        self.age = -1

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def get_sum(self, a, b):
        return a + b

    @staticmethod
    def get_class_name():
        return Person.__name__

    def __str__(self, *args, **kwargs):
        return 'this is Person class'
