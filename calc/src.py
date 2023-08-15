def plus_minus(li):

    for i in range(len(li)):
        print(li[i])
        try:
            li[i] = float(li[i])
        except ValueError:
            if li[i] == '-' or li[i] == '+': 
                li[i+1] = li[i] + li[i+1]
                li[i] = ''
    while '' in li:
        li.remove('')
    return li

tst = ['3','+','4','-','1','*','2','*','3','-','0']

print(plus_minus(tst))