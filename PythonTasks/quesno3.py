"""Question no-3.

Printing diamond pattern
"""


def diamond_pattern(num):
    """Func to print diamond pattern."""
    l_num = int(num/2)
    for i in range(0, num):
        if i <= l_num:
            print((l_num-i)*' '+(2*i+1)*'*')
        else:
            print((i-l_num)*' '+(2*(num-i-1)+1)*'*')


IPNUM = 0
while IPNUM % 2 == 0:
    IPNUM = int(input("enter any number: "))
    if IPNUM % 2 == 0:
        print("Please enter a odd number")

diamond_pattern(IPNUM)
