#!/usr/bin/python3
'''
    Rebel class!
'''


class MyInt(int):
    '''
        A rebel class. Bad class!!!
    '''
    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        return (self.value != value)

    def __ne__(self, value):
        return (self.value == value)
