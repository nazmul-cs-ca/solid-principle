'''
The Single-responsibility principle (SRP)

Befefits of SRP are followings
1. It is easier to localize errors. Any error in execution will point out to a smaller section of your code, accelerating your debug phase.
2. Any part of the code is reusable in other section of your code.
3. Moreover and, often overlooked, is that it is easier to create testing for each function of your code. 
   Side note on testing: You should write tests before you actually write the script. 
   But, this is often ignored in favour of creating some nice result to be shown to the stakeholders instead.
'''

import numpy as np

""" before compliant with SRP """
def math_operations(list_):
    # Compute Average
    print("the mean is {}".format(np.mean(list_)))

    # Compute Max
    print("the max is {}".format(np.max(list_))) 


""" after compliant with SRP """
def get_mean(list_):
    '''Compute Mean'''
    print("the mean is {}".format(np.mean(list_)))

def get_max(list_):
    '''Compute Max'''
    print("the max is {}".format(np.max(list_)))

if __name__ == "__main__":
    print("Hello from " + __file__ + " " + __name__)
    ''' not compliant with SRP '''
    math_operations(list_ = [1,2,3,4,5])
    
    ''' compliant with SRP '''
    list = [1,2,3,4,5]
    get_mean(list)
    get_max(list)



