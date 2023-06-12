#!/usr/bin/python3
'''
    A class that inherits from list
'''


class MyList(list):
    '''
        Inherits from list and prints sorted list.
    '''
    def print_sorted(self):
        '''
            Prints sorted list.
        '''
        print(sorted(self))
