# homework-2
project#2.py
# כדי להתשמש בלולאות שיש המון נתונים זה נותן לנו יכלות לקחת מבנה נתונים בדרך קצרה

#syntax: for y in x :

'''
#3
nunbers =[1,5,7,8,100]
for nunber in nunbers:
    print(nunbers[: len(nunbers) // 2:])
    if nunbers ==nunbers:
        break
'''

'''
#4
names=['hello','python','pen','world of coding']
for name in names:
    print(name.upper())
'''


'''
#5
names=['hello','python','pen','world of coding']
sum=4

for name in names:
    print(name)
    y=(len(name))
    print(y)
    if sum>y:
        break
'''
'''
#6
fullname="Yaniv Itzhak"

print(fullname[:6])
print(fullname[: len(fullname) // 3:])
print(fullname.count("a"))
print('b' in fullname)
print(fullname.split())
print(fullname[::-1])
x=fullname.split()
y=print(x[0] + x[1].upper())

'''

'''
#7
x="Hellow world!"
a=(x.index('o'))
print('The index of i:', a)
b=(x.index('o',5))
print('The index of i:', b)
x.split()
print(x[:5])
print(x[8:15])
original="Hellow world!"
removed = original.replace("o", "")
print(removed)
'''



'''
#9
numbers =[8, 1000, -3, 2, 5]
sum=0
for number in numbers:
    sum=sum + number
    print(f'{number} sum ={sum}')
x=print(sum)
print(max(numbers))
print(min(numbers))
for total in numbers:
    sum = sum + total
avg = sum / len(numbers)
print(f'average : {avg}')
numbers.remove(-3)
print(numbers)
numbers.sort()
print(numbers)
del numbers[0]
print(numbers)
# not working split
'''

#10
'''
numbers = [1,5,7,8,100]
x=0
for number in numbers:
    if x < number:
        x =number
print(number)
'''
