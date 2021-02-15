import time


class User:
    '''This class provides methods to initialize variables and print message'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_message(self):
        '''This method prints message using passed values for arguments name and age '''
        time.sleep(self.age)
        print("Hi {}, age: {}".format(self.name, self.age))
