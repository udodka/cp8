A = True
while A:
    try:
        n = int(input("введите десятичное число:"))
        s = int(input("введите систему счисления, в которую необходимо перевести число:"))
    except ValueError:
        print('еррор')
    else:
        A = False
if (s != 2 or s != 8) and (n <= 0):
    print("еррор")
elif s == 2:
    figure_2 = ""
    N = n
    while N > 0:
        figure_2 = str(N % 2) + figure_2
        N = N // 2
    print("вывод: ",n ,"->", figure_2)
elif s == 8:
    figure_8 = oct(n)[2::]
    print("вывод: ",n ,"->", figure_8)
