

class ClassSample:
    def __init__(self, instance_name):
        self.instance_name = instance_name

    @staticmethod
    def get_class_name():
        return ClassSample.__name__

    def get_instance_name(self):
        return self.instance_name
