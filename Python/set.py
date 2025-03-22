

a= {'mango', 'apple', 'banana'}

a.add('orange')
a.add(2)

a.update({9})
print(a)

# map

m= {'r':'ali', 2:'ahmed', 3:'ather'}

data=m.get('r')

data=m[2]


# print(m.items())

# print(m.keys())

# print(m.values())

# print('from map:',data)

m[2]='mubashir'
m['4']='khan'
print(m)

m.update({5:'lahore'})
m.pop(3)

print(len(m))
if 2 in m:
    print('yes')

for key, value in m.items():
    print(key,":", value)