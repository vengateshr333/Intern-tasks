"""Quesno:2.

List comprehension to get square of numbers
"""


def evensquare(num):
    """For even sq using list comprehension."""
    my_list = [i**2 for i in list(range(0, 2*num, 2))]
    return my_list


number = int(input('Enter the no of even number required:'))
out = evensquare(number)
print(out)
