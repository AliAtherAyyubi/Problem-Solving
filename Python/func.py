
def factorial(n):

    fact=1
    for i in range(n,1,-1):
        fact *=i
    return fact

def display(name):
    print(name)

display("ali ather")

def even():
    for i in range(0,15):
        if(i%2==0):
            print("Even Number:",i)

# even()

strs = ["flower","flow","flight"]
print(len(strs[0]))
print(strs[0][1])