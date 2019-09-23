
#using for
for i in range(1, 101):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 and i % 5 == 0:
        print('fizz buzz')
    else:
        print(i)

#using while
i = 0
while i < 100:
    i += 1
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 and i % 5 == 0:
        print('fizz buzz')
    else:
        print(i)