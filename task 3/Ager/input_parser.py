import argparse

class MyArgumentParser(argparse.ArgumentParser):
    def error(self,message=None):
        print('Argument Error')
        exit(2)

class InputParser():
    '''This class provides a CLI parser for arguments(name, age) using argparse module'''
    def __init__(self):
        parser = MyArgumentParser()
        parser.add_argument('-name', action='store', type=str, help='User name', required=True)
        parser.add_argument('-age', action='store', type=int, help="User's age", required=True)
        self.args = parser.parse_args()

    def get_name(self):
        return self.args.name

    def get_age(self):
        return self.args.age