

def reverse( x):
    # sign=0
    if x < 0:
        sign = -1
    else:
        sign = 1

    x = abs(x)

    x=str(x)

    x= x[::-1]

    x=int(x) *sign

    if x >= (-2**31) and x<=(2**31-1):
        return x
    return 0


# print(reverse(-856))\\

