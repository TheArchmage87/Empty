QA = input('About how long do you want your work peiriods to be?')
QA = int(QA)

A = []
a = []
c = input('How many classes homework do have to do?')
c = int(c)
for i in range(c):
    B = input('What homework do you have?')
    A.append(B)
    b = input('How long will it take?')
    a.append(b)

Y = []
y = []
x = input('How many subjects do you need to study for?')
x = int(x)
for i in range(x):
    Z = input('Which subject are you studying?')
    Y.append(Z)
    z = input('For how long?')
    y.append(z)

g = len(a)+1
h = len(y)+1
e = 0
f = 0
k = 0
j = 0
m = 0
n = 0
if len(a)>=len(y):
    for n in range(len(a)):
        if f < g:
            d = int(a[f])
            e = e+d
            if e > QA and f+k == 0:
                print(A[f])
            elif e > QA:
                print('break')
                print(A[f])
                e = d
            else:
                print(A[f])
            f = f+1
        
        if k < h:
            d = int(y[k])
            e = e+d
            if e > QA and f+k == 0:
                print(Y[k])
            elif e > QA:
                print('break')
                print(Y[k])
                e = d
            else:
                print(Y[k])
            k = k+1

if len(y)>len(a):
    for n in range(len(y)):
        if f < g:
            d = int(a[f])
            e = e+d
            if e > QA and f+k == 0:
                print(A[f])
            elif e > QA:
                print('break')
                print(A[f])
                e = d
            else:
                print(A[f])
            f = f+1
        
        if k < h:
            d = int(y[k])
            e = e+d
            if e > QA and f+k == 0:
                print(Y[k])
            elif e > QA:
                print('break')
                print(Y[k])
                e = d
            else:
                print(Y[k])
            k = k+1