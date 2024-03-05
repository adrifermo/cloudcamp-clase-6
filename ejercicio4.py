import sys
from math import pi, e
#from operations import factorial as fact

def echo_double(num, msg='Double of {0} is: {1}'):
    """
    Double a number an outputs its result
    """
    num = round(num, 2)
    print(msg.format(num, num * 2))


print('You\'re running on: {0}'.format(sys.platform))
echo_double(pi)
echo_double(e)
#print('factorial({0}): {1}'.format(5, fact(5)))ck