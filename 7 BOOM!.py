n = int(input('please insert number to count up to: \n'))
for i in range(1, n + 1):
    if (i % 7 ==0) or '7' in str (i) :
        print('BOOM!')

    else:
        print(i)
