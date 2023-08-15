def plus_minus(li:list):

    for i in range(len(li)):
        try:
            li[i] = float(li[i])
        except ValueError:
            if li[i] == '-' or li[i] == '+': 
                li[i+1] = li[i] + li[i+1]
                li[i] = ''
    while '' in li: li.remove('')
    return li

def mult_div(li:list):
    while ('*' in li) or ('/' in li):
        i = 0
        j = 0
        if '*' in li:
            i = li.index('*')
        if '/' in li:
            j = li.index('/')

        # print(str(i) + 'i__j' + str(j))

        if (i < j and i != 0) or j == 0:
            product = li[i-1] * li[i+1]
            li[i-1:i+2] = [product]
            # print('prod')
        elif (i > j and j != 0) or i == 0:
            ratio = li[j-1] / li[j+1]
            li[j-1:j+2] = [ratio]
            # print('ratio')
        else:
            raise Exception('i = j. Call tech support')

        # print(li)

    if ('/' or '*') in li:
        raise Exception('Multiplication and division went terribly wrong')

    return li



# tst = ['3','+','4','-','1','*','2','*','3','/','2','*', '2', '-', '4', '/', '5']

# plmi = [3.0, 4.0, -1.0, '/', 2.0,  '*', 2.0, -5.0, '/', 5.0, '*' , 5.0, -1.0, '*', 2.0, -4.0, '/', 5.0]
# # plmi = [3.0, 4.0, -1.0, '*', 2.0, -4.0, '/', 5.0]

# # print(plus_minus(tst))

# # ready = plus_minus(tst)
# print(mult_div(plmi))