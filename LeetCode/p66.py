

def plusOne(digits):
    if digits[-1] < 10:
        number = 0
        for i in digits:
            number = number * 10 + i
        number += 1
        number = str(number)
        digits = [int(i) for i in number]
    return digits


if __name__ == "__main__":

    print(plusOne([1,4,3]))

   
