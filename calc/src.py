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
        if i == 0 and j ==0: Exception('i = j. Call tech support') 

        elif (i < j and i != 0) or j == 0:
            product = li[i-1] * li[i+1]
            li[i-1:i+2] = [product]

        elif (i > j and j != 0) or i == 0:
            ratio = li[j-1] / li[j+1]
            li[j-1:j+2] = [ratio]

        else:
            raise Exception('idk. Call tech support?')
        
    if ('/' or '*') in li:
        raise Exception('Multiplication and division went terribly wrong')

    return li

def brackets(li:list):
    while ('(' in li) and (')' in li):
        cl = li.index(')')
        rev_li = li[0:cl]
        rev_li.reverse()
        op = rev_li.index('(')
        res = li[cl-op:cl]
        li[(cl-op)-1:cl+1] = [res]

    return li






tst = ['3','+','(','4','-', '(','1','*','2', ')', '*','3', ')','/','2','*', '(', '2', '-', '4', ')', '/', '5']

# plmi = [3.0, 4.0, -1.0, '/', 2.0,  '*', 2.0, -5.0, '/', 5.0, '*' , 5.0, -1.0, '*', 2.0, -4.0, '/', 5.0]
# # plmi = [3.0, '(', 4.0, -1.0, '*', 2.0, -4.0, '/', 5.0]           9+20-(4+3-(6*8)+3)-10 

print(brackets(tst))
# print(tst.reverse())

# # ready = plus_minus(tst)
# print(mult_div(plmi))